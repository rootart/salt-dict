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


require ['jquery', 'underscore', 'backbone'],($, _, Backbone)->
  console.log 'Loading application ...'

  class AppRouter extends Backbone.Router
    routes:
      "*actions": 'defaultRoute'

  router = new AppRouter;
  router.on 'route:defaultRoute',(actions)->
    alert(actions)
    return
  
  Backbone.history.start() 
  return