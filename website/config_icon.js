let icon_link = document.querySelector("link[rel~='icon']");
icon_link = document.createElement('link');
icon_link.rel = 'icon';
document.head.appendChild(icon_link);
icon_link.href = 'https://cdn-icons-png.flaticon.com/512/4718/4718900.png';