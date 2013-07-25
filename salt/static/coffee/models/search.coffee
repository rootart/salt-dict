define ['backbone', 'underscore', 'jquery'], (Backbone, _, $)->
  class SearchItemModel extends Backbone.Model
    defaults:
      "id": ""
      "definition": ""
