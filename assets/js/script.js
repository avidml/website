feather.replace()

let theme = localStorage.getItem('data-theme')

const changeThemeToDark = () => {
  document.getElementById('lightIcon').setAttribute('style', 'display:none')
  document.getElementById('darkIcon').setAttribute('style', 'display:inline-block')
  document.documentElement.setAttribute('data-theme', 'dark') // set theme to dark
  localStorage.setItem('data-theme', 'dark') // save theme to local storage
}

const changeThemeToLight = () => {
  document.getElementById('darkIcon').setAttribute('style', 'display:none')
  document.getElementById('lightIcon').setAttribute('style', 'display:inline-block')
  document.documentElement.setAttribute('data-theme', 'light') // set theme light
  localStorage.setItem('data-theme', 'light') // save theme to local storage
}
if (theme === 'light') {
  changeThemeToLight()
} else {
  changeThemeToDark()
}
const checkbox = document.getElementById('switch')
// Check current Theme from Local Storage
checkbox.addEventListener('change', () => {
  let theme = localStorage.getItem('data-theme')
  if (theme === 'dark') {
    changeThemeToLight()
  } else if (theme === 'light') {
    changeThemeToDark()
  }
})

const mobileNav = document.getElementById('mobileNav')
const menuOpen = document.getElementById('menuOpen')
const menuClose = document.getElementById('menuClose')
mobileNav.style.display = 'none'
menuClose.style.display = 'none'
menuOpen.style.display = 'block'

const resizeListener = () => {
  if (window.innerWidth > 576) {
    mobileNav.style.display = 'none'
    menuClose.style.display = 'none'
    menuOpen.style.display = 'block'
  }
}

window.addEventListener('resize', resizeListener)

const openMobile = () => {
  if (mobileNav.style.display === 'none') {
    mobileNav.style.display = 'block'
    menuOpen.style.display = 'none'
    menuClose.style.display = 'block'
  } else {
    mobileNav.style.display = 'none'
    menuClose.style.display = 'none'
    menuOpen.style.display = 'block'
  }
}

// Apply color-coded badges to report type column in database tables
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.avid-report-table tbody tr').forEach(function (row) {
    var td = row.cells[2]
    if (td) {
      var type = td.textContent.trim()
      if (type) {
        var typeClass = 'badge-' + type.toLowerCase().replace(/\s+/g, '-')
        td.innerHTML = '<span class="report-badge ' + typeClass + '">' + type + '</span>'
      }
    }
  })
})
