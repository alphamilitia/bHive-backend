// Initialize Firebase
  var config = {
    apiKey: "AIzaSyANras2IWcKPjyPHJ49Gvq_dgSbmMqq7s0",
    authDomain: "bhive-31d82.firebaseapp.com",
    databaseURL: "https://bhive-31d82.firebaseio.com",
    projectId: "bhive-31d82",
    storageBucket: "bhive-31d82.appspot.com",
    messagingSenderId: "550067182161"
  };
  firebase.initializeApp(config);

//Listen for signin button
btnlogin.addEventListener('click', submitForm);

//signin
function submitForm(){

	//test for submit function
	console.log(123);

	//get values
	var txtemail = getInputVal('txtemail');
	var txtpassword = getInputVal('txtpassword');
	var auth = firebase.auth();

	//test for var capture
	console.log(txtemail);

	//signin
	var promise = auth.signInWithEmailAndPassword(txtemail, txtpassword);
	promise.catch(e=>console.log(e.message));
};

//add a realtime listener to see if user logged in
firebase.auth().onAuthStateChanged(firebaseUser=>{
	if(firebaseUser){
		console.log(firebaseUser);
	} else{
		console.log('not logged in');
	}
	});


//function to get form values
function getInputVal(id){
	return document.getElementById(id).value;
}
