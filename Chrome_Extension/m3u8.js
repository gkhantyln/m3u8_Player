window.onload = function () {
    // get m3u8 urls for current active tab
    window.bg_wnd = chrome.extension.getBackgroundPage();
    var m3u8_urls = window.bg_wnd.bg.get_m3u8_urls();

    // function render m3u8 urls list
    render_m3u8_urls(m3u8_urls);
	  
};















function render_m3u8_urls(m3u8_urls) {
    var content = document.getElementById('content');

    if (!m3u8_urls || !m3u8_urls.length) {
        content.innerHTML = '<a href="player.html" target="_blank" class="books"><span class="mdi mdi-book mdi-18px" style=""><sup >M3U8 Adreslerim</sup></a><span class="mdi mdi-access-point-remove mdi-36px"  style="float:left;color:#666"></span><h5 class="not-found" style="color:#666;"> .m3u8 url bulunamadi</h5>';
        return;
    }
    
    var trs = [];
    for (var i = 0, cnt = m3u8_urls.length; i < cnt; i++) {
        var m3u8_url = m3u8_urls[i];
        trs.push('<a target="_blank" class="auto_start_download" title="auto start download" href="player.html#' + m3u8_url + '" ><div class="link" style=""><div style="float:left;"><span class="mdi mdi-play mdi-24px"></span></div>' + 
                 '<div class="content" style="line-height:26px;white-space: nowrap;" title="' + m3u8_url + '">' + m3u8_url + '</div></div></a>');
    }
    var download_all = '<a href="player.html" target="_blank" class="books"><span class="mdi mdi-book mdi-18px" style=""><sup>M3U8 Adreslerim</sup></a><br><span class="mdi mdi-access-point-check mdi-36px" style="float:left"></span><h5 class="found"><a class="download_all" title="download all" href="#">m3u8 urls:<b> ' + m3u8_urls.length + '</b></a></h5>';
    var auto_start_download_all = ((1 < m3u8_urls.length) ? '' : '');
    content.innerHTML = '<table><tr><td>' + auto_start_download_all + '</td><td>' + download_all + '</td></tr></table>' +
                        '<div class="content">' + trs.join('') + '</div>';

    
}

