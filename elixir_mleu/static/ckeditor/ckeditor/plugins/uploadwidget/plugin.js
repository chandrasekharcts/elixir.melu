﻿/*
 Copyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.
 For licensing, see LICENSE.md or http://ckeditor.com/license
*/
(function () {
    CKEDITOR.plugins.add("uploadwidget", {
        lang: "cs,da,de,en,eo,fr,gl,hu,it,ko,ku,nb,nl,pl,pt-br,ru,sv,tr,zh,zh-cn",
        requires: "widget,clipboard,filetools,notificationaggregator",
        init: function (b) {
            b.filter.allow("*[!data-widget,!data-cke-upload-id]")
        }
    });
    CKEDITOR.fileTools || (CKEDITOR.fileTools = {});
    CKEDITOR.tools.extend(CKEDITOR.fileTools, {
        addUploadWidget: function (b, c, a) {
            var f = CKEDITOR.fileTools,
                k = b.uploadRepository,
                m = a.supportedTypes ? 10 : 20;
            if (a.fileToElement) b.on("paste", function (i) {
                var i = i.data,
                    l = i.dataTransfer,
                    e = l.getFilesCount(),
                    j = a.loadMethod || "loadAndUpload",
                    d, g;
                if (!i.dataValue && e)
                    for (g = 0; g < e; g++) {
                        d = l.getFile(g);
                        if (!a.supportedTypes || f.isTypeSupported(d, a.supportedTypes)) {
                            var h = a.fileToElement(d);
                            d = k.create(d);
                            if (h) {
                                d[j](a.uploadUrl);
                                CKEDITOR.fileTools.markElement(h, c, d.id);
                                (j == "loadAndUpload" || j == "upload") && CKEDITOR.fileTools.bindNotifications(b, d);
                                i.dataValue = i.dataValue + h.getOuterHtml()
                            }
                        }
                    }
            }, null, null, m);
            CKEDITOR.tools.extend(a, {
                downcast: function () {
                    return new CKEDITOR.htmlParser.text("")
                },
                init: function () {
                    var a = this,
                        c = this.wrapper.findOne("[data-cke-upload-id]").data("cke-upload-id"),
                        e = k.loaders[c],
                        f = CKEDITOR.tools.capitalize,
                        d, g;
                    e.on("update", function (h) {
                        if (!a.wrapper || !a.wrapper.getParent()) {
                            b.editable().find('[data-cke-upload-id="' + c + '"]').count() || e.abort();
                            h.removeListener()
                        } else {
                            b.fire("lockSnapshot");
                            h = "on" + f(e.status);
                            if (!(typeof a[h] === "function" && a[h](e) === false)) {
                                g = "cke_upload_" + e.status;
                                if (a.wrapper && g != d) {
                                    d && a.wrapper.removeClass(d);
                                    a.wrapper.addClass(g);
                                    d = g
                                }(e.status ==
                                    "error" || e.status == "abort") && b.widgets.del(a)
                            }
                            b.fire("unlockSnapshot")
                        }
                    });
                    e.update()
                },
                replaceWith: function (a, c) {
                    if (a.trim() === "") b.widgets.del(this);
                    else {
                        var e = this == b.widgets.focused,
                            f = b.editable(),
                            d = b.createRange(),
                            g, h;
                        e || (h = b.getSelection().createBookmarks());
                        d.setStartBefore(this.wrapper);
                        d.setEndAfter(this.wrapper);
                        e && (g = d.createBookmark());
                        f.insertHtmlIntoRange(a, d, c);
                        b.widgets.checkWidgets({
                            initOnlyNew: true
                        });
                        b.widgets.destroy(this, true);
                        if (e) {
                            d.moveToBookmark(g);
                            d.select()
                        } else b.getSelection().selectBookmarks(h)
                    }
                }
            });
            b.widgets.add(c, a)
        },
        markElement: function (b, c, a) {
            b.setAttributes({
                "data-cke-upload-id": a,
                "data-widget": c
            })
        },
        bindNotifications: function (b, c) {
            var a = b._.uploadWidgetNotificaionAggregator;
            if (!a || a.isFinished()) {
                a = b._.uploadWidgetNotificaionAggregator = new CKEDITOR.plugins.notificationAggregator(b, b.lang.uploadwidget.uploadMany, b.lang.uploadwidget.uploadOne);
                a.once("finished", function () {
                    var c = a.getTaskCount();
                    c === 0 ? a.notification.hide() : a.notification.update({
                        message: c == 1 ? b.lang.uploadwidget.doneOne : b.lang.uploadwidget.doneMany.replace("%1",
                            c),
                        type: "success",
                        important: 1
                    })
                })
            }
            var f = a.createTask({
                weight: c.total
            });
            c.on("update", function () {
                f && c.status == "uploading" && f.update(c.uploaded)
            });
            c.on("uploaded", function () {
                f && f.done()
            });
            c.on("error", function () {
                f && f.cancel();
                b.showNotification(c.message, "warning")
            });
            c.on("abort", function () {
                f && f.cancel();
                b.showNotification(b.lang.uploadwidget.abort, "info")
            })
        }
    })
})();