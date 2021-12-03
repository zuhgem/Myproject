//odoo.define("crm_commission.action_manager", function (require) {
//
//
//var ActionManager = require('web.ActionManager');
//var framework = require('web.framework');
//var session = require('web.session');
//ActionManager.include({
//
//    /* execute actions of type ir.actions.report  */
//    _executexlsxReportDownloadAction: function (action) {
//        framework.blockUI();
//        var def = $.Deferred();
//        session.get_file({
//            url: '/xlsx_reports',
//            data: action.data,
//            success: def.resolve.bind(def),
//            complete: framework.unblockUI,
//        });
//        return def;
//    },
//
//
//    /* overrides to handle the ir.actions.report actions */
//
//
//    _executeReportAction: function (action, options) {
//        if (action.report_type === 'xlsx') {
//            return this._executexlsxReportDownloadAction(action, options);
//        }
//        return this._super.apply(this, arguments);
//    },
//});
//});