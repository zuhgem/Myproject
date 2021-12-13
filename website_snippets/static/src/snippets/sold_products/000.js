odoo.define('website_snippets.products', function (require) {
'use strict';

const publicWidget = require('web.public.widget');
const DynamicSnippetCarousel = require('website.s_dynamic_snippet_carousel');

publicWidget.registry.dynamic_snippet_products = DynamicSnippetCarousel.extend({
    selector: '.products',

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    _fetchData: async function () {
        const cards = await this._rpc({
            route: '/website_snippets/product',
        });
        this.data = [...$(cards)].filter(node => node.nodeType === 1).map(el => el.outerHTML);
    },
});
});
