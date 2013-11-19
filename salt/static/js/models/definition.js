// Generated by CoffeeScript 1.6.2
var __hasProp = {}.hasOwnProperty,
  __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

define(['backbone', 'underscore', 'jquery'], function(Backbone, _, $) {
  var DefinitionItemModel, _ref;

  return DefinitionItemModel = (function(_super) {
    __extends(DefinitionItemModel, _super);

    function DefinitionItemModel() {
      _ref = DefinitionItemModel.__super__.constructor.apply(this, arguments);
      return _ref;
    }

    DefinitionItemModel.prototype.defaults = {
      "id": "",
      "name_en": "",
      "name_de": "",
      "name_ru": "",
      "name_ru_slug": ""
    };

    return DefinitionItemModel;

  })(Backbone.Model);
});
