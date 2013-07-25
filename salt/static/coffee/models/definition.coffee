define ['backbone', 'underscore', 'jquery'], (Backbone, _, $)->
  class DefinitionItemModel extends Backbone.Model
    defaults:
      "id": ""
      "definition_en": ""
      "definition_de": ""
      "definition_ru": ""
