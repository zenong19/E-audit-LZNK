// Create App
const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data(){
        return {

        }
    },
    mounted: function() {
        // Calls the method before page loads
    },
    methods:{
        sendMemo(){
            let counter = document.getElementsByTagName('input').length;
            let emails = ""

            for (let i = 0; i < counter; i++) {
                if (document.getElementsByTagName('input')[i].checked == true) {
                    emails = emails + document.getElementsByTagName('input')[i].value + ",";
                }
            }

            let subject = 'New mail';
            let body = 'Terdapat senarai semak yang belum complete. http://eaudit-lznk.herokuapp.com/audit_userresponseMenu';

            let to = "mailto:" + emails + '?subject=' + subject + '&body=' + body;
            // console.log(to);
            window.open(to);
        },
    }
})