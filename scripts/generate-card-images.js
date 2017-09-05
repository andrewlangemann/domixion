/* generate-card-images.js

To be used on the Dominion Card Image Generator site to generate cards
based on JSON data and produce download links.

https://shemitz.net/static/dominion3/

*/

(function(){
    var setData = ''; //insert JSON here
    var cardCanvas = document.getElementById('portraitCanvas');
    for (var i = 0; i < setData.cards.length; i++) {
        var card = setData.cards[i];

        if (card['card-type'].startsWith('Action - Reaction')) {
            
        }
    };
})()
