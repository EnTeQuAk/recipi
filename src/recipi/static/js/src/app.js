import jquery from 'jquery';
import Backbone from 'backbone';
import Foundation from 'foundation';


$(() => {
	Backbone.$ = $;
	Backbone.history.start();

	Foundation.init();
});
