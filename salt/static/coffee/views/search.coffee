define ['backbone', 'underscore', 'jquery', 'models/search'], (Backbone, _, $, SearchItemModel)->
  class SearchView extends Backbone.View
    el: 'article.main'
    events:
      'keyup input[type=text]': 'searchDefinition'

    template: _.template("""
    <li><a href="#<%= name_en %>"><%= name_ru %></a></li>
    """)

    renderInitialResults: (item)->
      html = @.template item.attributes
      return html

    searchDefinition: ()->
      console.log 'searching...'
      q = @.$('input[type=text]').val()
      url = "/api/v1/search/?q="+q
      self = @

      $.get url,(data)->
        self.$('.vocabulary').html '' 
        for item in data.objects
          model = new SearchItemModel(item)
          self.$('.vocabulary').prepend self.renderInitialResults(model)
      return