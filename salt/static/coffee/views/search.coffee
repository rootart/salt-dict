define ['backbone', 'underscore', 'jquery'], (Backbone, _, $)->
  class SearchView extends Backbone.View
    class: 'article.main'
    events:
      'keyup input[type=text]': 'searchDefinition'

    tempalte: _.template("""
    <li><a href="#<%= definition %>"><%= definition %></a></li>
    """)
    renderSearchResults: ()->
      return

    searchDefinition: ()->
      console.log 'search'
      return