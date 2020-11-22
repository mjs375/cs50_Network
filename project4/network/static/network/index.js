// J A V A S C R I P T


function followToggle(username) {
  event.preventDefault() //prevent <a> from reloading page
  console.log("Following...", username)
  var count = document.querySelector('#followby').innerHTML;
  //
  // Toggle button display:
  if (event.srcElement.innerHTML == "Follow") {
    //Unfollow is displayed since you just followed:
    var btn = "Unfollow"
    //+1 to profile user's followers count (you:)
    count++;
  } else {
    //Follow:
    var btn = "Follow"
    //
    count--;
  }
  // Update the button (since page doesn't reload):
  event.srcElement.innerHTML = btn;
  // Update the profile user's follower count:
  document.querySelector('#followby').innerHTML = count
  //Update actual database:
  follow(username);
} // * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


function follow(username) {
  event.preventDefault()
  console.log("Fetching...",username)
  console.log("Fetching...")
  fetch(`addfollow/${username}`, {
    method: 'PUT',
  });

} // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *



function likeToggle(likebutton) { // Toggle 'Like'/'Unlike'
  event.preventDefault()
  // GET ID of OVERALL POST DIV (holds all contents of one single post, id = post.id)
  const post_parent_id = likebutton.parentNode.parentNode.getAttribute('id')
  var likescount = document.querySelector(`#likes-${post_parent_id}`).innerHTML;
  //
  if (likebutton.innerHTML == "Like") { //--Unlike Path
    //--Change button
    event.srcElement.innerHTML = "Unlike";
    like(post_parent_id); //CALL F(X) TO ACTUALLY CHANGE DB LIKES
    //-Update counter on page (to show since page not auto-reloaded)
    likescount++;
  } else { //--Like Path
    //--Change button
    event.srcElement.innerHTML = "Like";
    like(post_parent_id); //CALL F(X) TO ACTUALLY CHANGE DB LIKES
    //--Update likes counter:
    likescount--;
  };
  //--Change the Likes counter:
  document.querySelector(`#likes-${post_parent_id}`).innerHTML = likescount;
} // * * * * * * * * * * * * * * * * * * * * * * *

function like(id) {
  console.log("Hey! Fetch PUT happening! + 1 like!")
  console.log(`${id}`)
  fetch(`/like/${id}`, {
    method: 'PUT',
  });
}














function editPost(obj) {
  //--Create a textarea element, add attributes:
  const id = event.srcElement.parentNode.parentNode.getAttribute('id')
  console.log("LooK! AN ID:", id)

  const edit_box = document.createElement('TEXTAREA');
  edit_box.className = 'textarea-edit only-one';
  edit_box.setAttribute('id',`x${id}`)  // set identifying 'id'=post(id) to help cancelEdit() function
  //--Populate new textarea with old message to be edited:
  old_msg = document.querySelector(`#body-${id}`).innerHTML;
  edit_box.innerHTML = old_msg;
  //--Create Submit button, add attributes:
  const submit_btn = document.createElement('input');
  submit_btn.setAttribute('type', 'submit');
  submit_btn.setAttribute('value', 'Submit');
  submit_btn.className = `${id} only-one submitEdit`;
  submit_btn.setAttribute('id',`y${id}`)  // set identifying 'id'=post(id) to help cancelEdit() function
  //--Change 'Edit' button to 'Cancel' button:
  event.srcElement.innerHTML= 'Cancel';
  event.srcElement.setAttribute('onclick', 'cancelEdit(this)');
  //--Hide post's message (textarea 'replaces' its spot):
  document.querySelector(`#body-${id}`).style.display = 'none'; //
  // Add the elements to the webpage
  document.querySelector(`#edit-${id}`).append(edit_box);
  document.querySelector(`#edit-${id}`).append(submit_btn);
  // Event Listener for submit button clicked
  document.querySelector('.submitEdit').addEventListener('click', () => submitEdit(id));
} // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *










function cancelEdit() { // Close any rough drafts...
  // srcElement = submit-btn (id=id)
  event.srcElement.innerHTML = 'Edit';
  //--Get ID of parent node (entire single post div is id=id):
  //id = event.srcElement.id
  const id = event.srcElement.parentNode.parentNode.getAttribute('id')
  console.log("HEY",id)
  event.srcElement.setAttribute('onclick', 'editPost(this)')
  //--Empty the enclosing div, thus erasing the <textarea>
  old_msg = document.querySelector(`#x${id}`).innerHTML;
  document.querySelector(`#body-${id}`).style.display = 'inline'; //
  document.querySelector(`#body-${id}`).innerHTML = old_msg;
  document.querySelector(`#edit-${id}`).innerHTML = ""
} // * * * * * * * * * * * * * * * * * * * * * * * *


function submitEdit(id) {
  //--Update the SQUEAK:
  console.log("submitEdit:", id); // const test = event.srcElement.className
  const new_msg = document.querySelector(`#x${id}`).value;
  console.log(new_msg);
  //--Save the Edited Post:
  fetch(`/edit/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      message: new_msg
    })
  });
  //* * * * * * * *//
  // Remove <textarea>/<submit> button:
  console.log(document.querySelector(`#edit-${id}`).innerHTML)
  document.querySelector(`#edit-${id}`).innerHTML = ""
  // Restore message field w/ NEW message:
  document.querySelector(`#body-${id}`).style.display = 'block';
  document.querySelector(`#body-${id}`).innerHTML = new_msg;
  // Change name/onclick of 'Cancel' button back to 'Edit'
  document.getElementById(`btn-${id}`).innerHTML = 'Edit';
  document.getElementById(`btn-${id}`).setAttribute('onclick', 'editPost(this)');

} // * * * * * * * * * * * * * * * * *



// COUNT CHARS LEFT IN SQUEAK MESSAGE (0/160):
function myCounter(obj) {
  var max = 160;
  var length = obj.value.length;
  var charleft = (max - length);
  // console.log(max, length, charleft)
  //
  if (length === 0) {
    document.getElementById("count").innerHTML = ""
  }
  else if (length < max) { //turn text red if over max limit
    document.getElementById("count").innerHTML = charleft + " characters left.";
  } else { //otherwise just display a count
    document.getElementById("count").innerHTML = "All out of room, squeaker!"
  };
}; // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
