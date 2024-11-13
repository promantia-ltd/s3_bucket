// frappe.ui.form.on("File", {
//     refresh: function (frm) {
//         if (frm.doc.file_url) {
//             frm.fields_dict['file_url'].wrapper.innerHTML = `<a href="${frm.doc.file_url}" target="_blank">${frm.doc.file_url}</a>`;
//             frm.refresh_field('file_url');
//         }
//     }
// });

// frappe.ui.form.on("File", {
//     refresh: function (frm) {
//         if (frm.doc.file_url) {
//             const linkHtml = `<a href="${frm.doc.file_url}" target="_blank">${frm.doc.file_url}</a>`;

//             // Create a custom button or text field below the file_url field (without affecting the original field)
//             frm.add_custom_button(__('Open File'), function () {
//                 window.open(frm.doc.file_url, '_blank');
//             });
            
//         }
//     }
// });

frappe.ui.form.on("File", {
    refresh: function (frm) {
        if (frm.doc.file_url) {
            // Set the field to read-only to display URL as plain text
            frm.set_df_property('file_url', 'read_only', 1);
            frm.refresh_field('file_url');

            // Set the value of the file_url field as plain text
            frm.set_value('file_url', frm.doc.file_url);

            // Create a button next to the field for opening the link
            if (!frm.fields_dict['file_url'].wrapper.querySelector('.open-link-btn')) {
                $(frm.fields_dict['file_url'].wrapper).append(`
                    <button class="btn btn-xs btn-link open-link-btn" style="margin-left: 5px;" onclick="window.open('${frm.doc.file_url}', '_blank')">
                        Open Link
                    </button>
                `);
            }
        }
    }
});
