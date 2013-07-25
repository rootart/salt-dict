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


require ['jquery', 'underscore', 'backbone', 'views/search'],($, _, Backbone, SearchView)->
  console.log 'Loading application ...'

  class AppRouter extends Backbone.Router
    routes:
      "/": 'indexPage'
      "*actions": 'defaultRoute'
 
  router = new AppRouter;
  router.on 'route:indexPage', (actions)->
    alert 'index'
  router.on 'route:defaultRoute',(actions)->
    alert(actions)
    return

  search  = new SearchView()
  Backbone.history.start() 
  return