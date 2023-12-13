"use strict";
(function () {
    CKEDITOR.plugins.add("uploadimage", {
        requires: "uploadwidget",
        onLoad: function () {
            CKEDITOR.addCss(".cke_upload_uploading img{opacity: 0.3}")
        },
        init: function (b) {
            if (!CKEDITOR.plugins.clipboard.isFileApiSupported) {
                return
            }
            var d = CKEDITOR.fileTools,
                c = d.getUploadUrl(b.config, "image");
            if (!c) {
                CKEDITOR.error("uploadimage-config");
                return
            }
            d.addUploadWidget(b, "uploadimage", {
                supportedTypes: /image\/(jpeg|png|gif|bmp)/,
                uploadUrl: c,
                fileToElement: function () {
                    var e = new CKEDITOR.dom.element("img");
                    e.setAttribute("src", a);
                    return e
                },
                parts: {
                    img: "img"
                },
                onUploading: function (e) {
                    this.parts.img.setAttribute("src", e.data)
                },
                onUploaded: function (e) {
                    console.log(e);
                    this.replaceWith('<img src="' + e.url + '" width="' + this.parts.img.$.naturalWidth + '" height="' + this.parts.img.$.naturalHeight + '">')
                }
            });
            b.on("paste", function (m) {
                if (!m.data.dataValue.match(/<img[\s\S]+data:/i)) {
                    return
                }
                var h = m.data,
                    l = document.implementation.createHTMLDocument(""),
                    o = new CKEDITOR.dom.element(l.body),
                    j, f, g;
                o.data("cke-editable", 1);
                o.appendHtml(h.dataValue);
                j = o.find("img");
                for (g = 0; g < j.count(); g++) {
                    f = j.getItem(g);
                    var k = f.getAttribute("src") && f.getAttribute("src").substring(0, 5) == "data:",
                        e = f.data("cke-realelement") === null;
                    if (k && e && !f.data("cke-upload-id") && !f.isReadOnly(1)) {
                        var n = b.uploadRepository.create(f.getAttribute("src"));
                        n.upload(c);
                        d.markElement(f, "uploadimage", n.id);
                        d.bindNotifications(b, n)
                    }
                }
                h.dataValue = o.getHtml()
            })
        }
    });
    var a = "data:image/gif;base64,R0lGODlhDgAOAIAAAAAAAP///yH5BAAAAAAALAAAAAAOAA4AAAIMhI+py+0Po5y02qsKADs="
})();