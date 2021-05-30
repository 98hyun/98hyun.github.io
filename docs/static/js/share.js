function kakao() {
  const title = document.querySelector('meta[property="og:title"]')["content"];
  const desc = document.querySelector('meta[property="og:description"]')["content"];
  const img = document.querySelector('meta[property="og:image"]')["content"];;
  const url = window.location.href;

  Kakao.init('f46f40e1f3ada79ccc0780daaac6cc92')
  Kakao.Link.sendDefault({
    objectType: 'feed',
    content: {
      title: title,
      description: desc,
      imageUrl: img,
      link: {
        mobileWebUrl: url,
        webUrl: url,
      },
    },
    buttons: [
      {
        title: '웹으로 보기',
        link: {
          mobileWebUrl: url,
          webUrl: url,
        },
      }
    ]
  })
}

(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0";
  fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));