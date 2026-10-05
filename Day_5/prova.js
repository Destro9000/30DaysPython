const mainSec = document.getElementById('main-section');
const formSec = document.getElementById('form-section');
const addBookmarkBtn = document.getElementById('add-bookmark-button');
const category = document.querySelector('.category-name')
const catDropDown = document.getElementById('category-dropdown');
const closeFormBtn = document.getElementById('close-form-button');
const addBookmarkFormBtn = document.getElementById('add-bookmark-button-form');
const nameBookmark = document.getElementById('name');
const urlBookmark = document.getElementById('url');
const bookmarkSec = document.getElementById('bookmark-list-section');
const viewCatBtn = document.getElementById('view-category-button');



let isFormHidden = true;



function getBookmarks(){
  const bookmarks = JSON.parse(localStorage.getItem('bookmarks')) || []; 
  if(!bookmarks){
    return [];
  }

  return bookmarks;
}



function displayOrCloseForm(){
  mainSec.classList.toggle('hidden');
  formSec.classList.toggle('hidden');

}


function displayOrHideCategory(){
  mainSec.classList.toggle('hidden');
  bookmarkSec.classList.toggle('hidden');
}
addBookmarkBtn.addEventListener("click", () => {
  category.innerText = catDropDown.value;
  displayOrCloseForm();


  
})

closeFormBtn.addEventListener('click', () => {
  displayOrCloseForm();
})

addBookmarkFormBtn.addEventListener('click', () => {

  const bookmarks = getBookmarks();
  bookmarks.push({
    name: nameBookmark.value,
    category: catDropDown.value,
    url:urlBookmark.value,
  })

  localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
  
  nameBookmark.value = '';
  urlBookmark.value = '';

  displayOrCloseForm();


})

viewCatBtn.addEventListener('click', () => {
  category.innerText = catDropDown.value;
  
})