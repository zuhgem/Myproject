odoo.define('website_snippets.snippet.options', function (require) {
'use strict';

const options = require('web_editor.snippets.options');

options.registry.ViewProductsOptions = options.Class.extend({
    //--------------------------------------------------------------------------
    // Options
    //--------------------------------------------------------------------------

    /**
     * @see this.selectClass for parameters
     */
    logStuff(previewMode, widgetValue, params) {
        console.log(previewMode, widgetValue, params);
    }
});
});
