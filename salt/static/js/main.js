// Generated by CoffeeScript 1.6.2
var __hasProp = {}.hasOwnProperty,
  __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

require.config({
  paths: {
    jquery: 'vendor/jquery-1.9.1',
    underscore: 'vendor/underscore',
    backbone: 'vendor/backbone'
  },
  shim: {
    backbone: {
      deps: ['jquery', 'underscore'],
      exports: 'Backbone'
    },
    underscore: {
      exports: '_'
    }
  }
});

require(['jquery', 'underscore', 'backbone', 'views/search', 'models/search', 'models/definition', 'views/details'], function($, _, Backbone, SearchView, SearchItemModel, DefinitionItemModel, DetailView) {
  var AppRouter, router, search, searchView, _ref;

  console.log('Loading application ...');
  AppRouter = (function(_super) {
    __extends(AppRouter, _super);

    function AppRouter() {
      _ref = AppRouter.__super__.constructor.apply(this, arguments);
      return _ref;
    }

    AppRouter.prototype.routes = {
      "": 'indexPage',
      ":definition": 'definitionDetails'
    };

    return AppRouter;

  })(Backbone.Router);
  router = new AppRouter;
  searchView = new SearchView();
  router.on('route:indexPage', function(actions) {
    var url;

    url = '/api/v1/definitions/?format=json';
    $.get(url, function(data) {
      var item, model, _i, _len, _ref1, _results;

      _ref1 = data.objects;
      _results = [];
      for (_i = 0, _len = _ref1.length; _i < _len; _i++) {
        item = _ref1[_i];
        model = new SearchItemModel(item);
        _results.push(searchView.$('.vocabulary').prepend(searchView.renderInitialResults(model)));
      }
      return _results;
    });
  });
  router.on('route:definitionDetails', function(actions) {
    var url;

    url = '/api/v1/search/' + actions + '/';
    return $.get(url, function(data) {
      var details, model;

      model = new Backbone.Model(data);
      details = new DetailView({
        'model': model
      });
      return $('.value').html(details.renderItem());
    });
  });
  search = new SearchView();
  Backbone.history.start();
});
