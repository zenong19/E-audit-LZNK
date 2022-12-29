// Create App
const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data(){
        return {
            userid: "",
            username:"",
            password:"",
            gender:"",
            email:"",
            contact:"",
            num: "",
            access1:"",
            access2:"",
            access3:"",
            access4:"",
            date:"",
        }
    },
    mounted: function() {
        // Calls the method before page loads
        this.getData();
    },
    methods:{
        OnSubmit(){
            if (this.$refs.userid.value == "") {
                alert("ID must be filled out");
                return false;
            } else if (this.username == "") {
                alert("Name must be filled out");
                return false;
            } else if (this.password == "") {
                alert("Password must be filled out");
                return false;
            } else if (this.gender == "") {
                alert("Gender must be filled out");
                return false;
            } else if (this.email == "") {
                alert("Email must be filled out");
                return false;
            } else if (this.contact == "") {
                alert("Contact must be filled out");
                return false;
            } else if (this.date == "") {
                alert("Date must be filled out");
                return false;
            } else {
                this.$refs.form.submit();
            }
        },
        getData(){
            const nama = document.getElementById('name').innerText;
            this.userid = document.getElementById(nama).cells[0].innerHTML;
            this.username = nama;
            this.password = document.getElementById(nama).cells[1].innerHTML;
            this.gender = document.getElementById(nama).cells[2].innerHTML;
            this.email = document.getElementById(nama).cells[3].innerHTML;
            this.contact = document.getElementById(nama).cells[4].innerHTML;
            this.access1 = document.getElementById(nama).cells[5].innerHTML;
            if (this.access1 == 'admin') {
                document.getElementById("access1").checked = true;
            }
            this.access2 = document.getElementById(nama).cells[6].innerHTML;
            if (this.access2 == 'audit') {
                document.getElementById("access2").checked = true;
            }
            this.access3 = document.getElementById(nama).cells[7].innerHTML;
            if (this.access3 == 'management') {
                document.getElementById("access3").checked = true;
            }
            this.access4 = document.getElementById(nama).cells[8].innerHTML;
            if (this.access4 == 'setup') {
                document.getElementById("access4").checked = true;
            }
            this.date = document.getElementById(nama).cells[9].innerHTML;
        },
        OnDelete(){
            this.$refs.form.submit();
        },
    }
})