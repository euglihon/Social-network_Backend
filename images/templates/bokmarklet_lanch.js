(function() {
    let site_url = 'https://33b6305aefb0.ngrok.io';

    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src=site_url + '/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();