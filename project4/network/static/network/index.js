// J A V A S C R I P T

function editPost(obj) {
  //--Create a textarea element, add attributes:
  const edit_box = document.createElement('TEXTAREA');
  edit_box.className = 'textarea-edit only-one';
  edit_box.setAttribute('id',`x${obj.id}`)  // set identifying 'id'=post(id) to help cancelEdit() function
  //--Populate new textarea with old message to be edited:
  old_msg = document.querySelector(`#body-${obj.id}`).innerHTML;
  edit_box.innerHTML = old_msg;
  //--Create Submit button, add attributes:
  const submit_btn = document.createElement('input');
  submit_btn.setAttribute('type', 'submit');
  submit_btn.setAttribute('value', 'Submit');
  submit_btn.className = `${obj.id} only-one submitEdit`;
  submit_btn.setAttribute('id',`y${obj.id}`)  // set identifying 'id'=post(id) to help cancelEdit() function
  //--Change 'Edit' button to 'Cancel' button:
  event.srcElement.innerHTML= 'Cancel';
  event.srcElement.setAttribute('onclick', 'cancelEdit(this)');
  //--Hide post's message (textarea 'replaces' its spot):
  document.querySelector(`#body-${obj.id}`).style.display = 'none'; //
  // Add the elements to the webpage
  document.querySelector(`#edit-${obj.id}`).append(edit_box);
  document.querySelector(`#edit-${obj.id}`).append(submit_btn);
  // Event Listener for submit button clicked
  document.querySelector('.submitEdit').addEventListener('click', () => submitEdit(obj.id));
} // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

function cancelEdit() { // Close any rough drafts...
  // srcElement = submit-btn (id=id)
  event.srcElement.innerHTML = 'Edit';
  id = event.srcElement.id
  event.srcElement.setAttribute('onclick', 'editPost(this)')
  //--Empty the enclosing div, thus erasing the <textarea>
  old_msg = document.querySelector(`#body-${id}`).innerHTML;
  document.querySelector(`#body-${id}`).style.display = 'inline'; //
  document.querySelector(`#body-${id}`).innerHTML = old_msg;
  document.querySelector(`#edit-${id}`).innerHTML = ""

}


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
  document.querySelector(`#edit-${id}`).innerHTML = ""
  // Restore message field w/ NEW message:
  document.querySelector(`#body-${id}`).style.display = 'block';
  document.querySelector(`#body-${id}`).innerHTML = new_msg;
  // Change name/onclick of 'Cancel' button back to 'Edit'
  document.getElementById(id).innerHTML = 'Edit';
  console.log("X",)
  document.getElementById(id).setAttribute('onclick', 'editPost(this)');

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
