import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getFirestore, collection, addDoc, onSnapshot, query, orderBy, serverTimestamp, deleteDoc, doc } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyCHPbLci41UkzNCwCn6FzYQ5OgPBntwjYs",
  authDomain: "claw-f7b88.firebaseapp.com",
  projectId: "claw-f7b88",
  storageBucket: "claw-f7b88.firebasestorage.app",
  messagingSenderId: "598940134212",
  appId: "1:598940134212:web:dd95d66aafb05b65604511",
  measurementId: "G-6X5359W8XR"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const notesCollection = collection(db, "notes");

const input = document.getElementById("note-input");
const addBtn = document.getElementById("add-btn");
const list = document.getElementById("notes-list");

// Add a note
addBtn.addEventListener("click", async () => {
    const text = input.value.trim();
    if (text) {
        await addDoc(notesCollection, {
            text: text,
            createdAt: serverTimestamp()
        });
        input.value = "";
    }
});

// Listen for Enter key
input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") addBtn.click();
});

// Real-time listener for notes
const q = query(notesCollection, orderBy("createdAt", "desc"));
onSnapshot(q, (snapshot) => {
    list.innerHTML = "";
    snapshot.forEach((docSnap) => {
        const note = docSnap.data();
        const li = document.createElement("li");
        li.innerHTML = `
            <span>${note.text}</span>
            <button class="delete-btn" data-id="${docSnap.id}">Delete</button>
        `;
        list.appendChild(li);
    });

    // Add delete functionality
    document.querySelectorAll(".delete-btn").forEach(btn => {
        btn.addEventListener("click", async (e) => {
            const id = e.target.getAttribute("data-id");
            await deleteDoc(doc(db, "notes", id));
        });
    });
});