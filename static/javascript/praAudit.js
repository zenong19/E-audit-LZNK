// Create App
const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data(){
        return {
            dates:[],
        }
    },
    mounted: function() {
        // Calls the method before page loads
        var today = new Date();
        let year = today.getFullYear();
        let history = year-20;

        for (let index = 0; index <= 20; index++) {
            this.dates[index] = history++;
        }
    },
    methods:{
        searchDate(){
            let counter = document.getElementsByClassName('log').length;
            let date = '';

            for (let index = 0; index < document.getElementsByName('date')[0].length; index++) {
                if (document.getElementsByName('date')[0][index].selected) {
                    date = document.getElementsByName('date')[0][index].innerText;
                }
                
            }
            
            for (let i = 0; i < counter; i++) {
                if (document.getElementsByClassName('log')[i].outerText.substr(0, 4) == date) {
                    document.getElementsByClassName('log')[i].hidden = false;
                } else {
                    document.getElementsByClassName('log')[i].hidden = true;
                }
            }
        },
    }
})