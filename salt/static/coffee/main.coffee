require.config
  paths:
    jquery: 'vendor/jquery-1.9.1'
    underscore: 'vendor/underscore'
    backbone: 'vendor/backbone'
  shim:
    backbone:
      deps: ['jquery', 'underscore']
      exports: 'Backbone'
    underscore:
      exports: '_'


require ['jquery', 'underscore', 'backbone', 'views/search', 'models/search', 'models/definition'],($, _, Backbone, SearchView, SearchItemModel, DefinitionItemModel)->
  console.log 'Loading application ...'

  class AppRouter extends Backbone.Router
    routes:
      "": 'indexPage'
      ":definition": 'definitionDetails'

  router = new AppRouter;
  
  searchView = new SearchView()
  router.on 'route:indexPage', (actions)->
    url = '/api/v1/definitions/?format=json'

    $.get url,(data)->
      for item in data.objects
        model = new SearchItemModel(item)
        searchView.$('.vocabulary').prepend searchView.renderInitialResults(model)
    return

  router.on 'route:definitionDetails', (actions)->
    alert actions


  search  = new SearchView()
  Backbone.history.start() 
  return