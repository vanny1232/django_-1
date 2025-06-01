
    loding = document.querySelector(".loding");
    loader = document.querySelector('#loader');
    if (navigator.onLine) {
        showStatus(true);
    }else{
        showStatus(false);
    }
    function showStatus(isOnline) {
        if (isOnline){
            setTimeout(() => {
            loding.style.display = 'none';
            loader.style.display = 'none';
            }, 2000);
        }else {
            loding.style.display = 'flex';
            loader.style.display = 'inline-block';
        } 
    }
    // window.addEventListener('online', checkInternetConnection);
    // window.addEventListener('offline', checkInternetConnection);
    // setInterval(checkInternetConnection, 30000);