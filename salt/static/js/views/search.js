// Generated by CoffeeScript 1.6.2
var __hasProp = {}.hasOwnProperty,
  __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

define(['backbone', 'underscore', 'jquery', 'models/search'], function(Backbone, _, $, SearchItemModel) {
  var SearchView, _ref;

  return SearchView = (function(_super) {
    __extends(SearchView, _super);

    function SearchView() {
      _ref = SearchView.__super__.constructor.apply(this, arguments);
      return _ref;
    }

    SearchView.prototype.el = 'article.main';

    SearchView.prototype.events = {
      'keyup input[type=text]': 'searchDefinition'
    };

    SearchView.prototype.template = _.template("<li><a href=\"#<%= name_ru %>\"><%= name_ru %></a></li>");

    SearchView.prototype.renderInitialResults = function(item) {
      var html;

      html = this.template(item.attributes);
      return html;
    };

    SearchView.prototype.searchDefinition = function() {
      var q, self, url;

      console.log('searching...');
      q = this.$('input[type=text]').val();
      url = "/api/v1/definitions/?name_en__startswith=" + q + "&format=json";
      self = this;
      $.get(url, function(data) {
        var item, model, _i, _len, _ref1, _results;

        self.$('.vocabulary').html('');
        _ref1 = data.objects;
        _results = [];
        for (_i = 0, _len = _ref1.length; _i < _len; _i++) {
          item = _ref1[_i];
          model = new SearchItemModel(item);
          _results.push(self.$('.vocabulary').prepend(self.renderInitialResults(model)));
        }
        return _results;
      });
    };

    return SearchView;

  })(Backbone.View);
});
