define ['backbone', 'underscore', 'jquery'], (Backbone, _, $)->
  class DefinitionItemModel extends Backbone.Model
    defaults:
      "id": ""
      "name_en": ""
      "name_de": ""
      "name_ru": ""
