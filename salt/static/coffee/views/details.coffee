define ['backbone', 'underscore', 'jquery', 'models/search'], (Backbone, _, $, SearchItemModel)->
  class DetailView extends Backbone.View
    template: _.template """
        <ul>
           <li>
             <h2>
               <%= name_ru %> <span>( нем. <%= name_de %>, англ. <%= name_en %> )</span>
             </h2>
             <% _.each(sources, function(source) { %> 
             <article class="desc">
               <header>
                 <%= source.bib_info  %>
               </header>
               <p><%= source.text  %></p>
             </article>
            <% }); %>
           </li>
         </ul>
    """
    renderItem: ()->
      html = @.template @.model.attributes