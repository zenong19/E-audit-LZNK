// Create App
const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data(){
        return {
            a:true,
            b:true,
            date:[],
            staff:[],
            type:[],
            d:0,
        }
    },
    mounted: function() {
        // Calls the method before page loads
        // Extract Date
        for (let index = 0; index < $(".log")[0].children.length; index++) {
            this.date.push($(".log")[0].children[index].children[0].innerText.slice(0, 4));
        }
        // sort by years
        this.date.sort(function(a, b){return a - b});
        // remove duplicates
        const years = new Set(this.date);
        this.date = [];
        years.forEach(v => this.date.push(v));

        // console.log(this.date);
        // console.log(this.staff);
    },
    methods:{
        print(){
            console.log();
            
            document.getElementsByClassName('split left')[0].hidden = true;
            document.getElementById('options').style.display = 'none';
            document.getElementById('printer').style.display = 'none';
            document.getElementsByClassName('split right')[0].style.width = '100%';
            window.print()
            document.getElementsByClassName('split left')[0].hidden = false;
            document.getElementById('options').style.display = 'grid';
            document.getElementById('printer').style.display = 'grid';
            document.getElementsByClassName('split right')[0].style.width = '75%';
        },
        dateSelect() {
            this.staff = [];
            this.type = [];
            // Find audit within selected year
            // Extract Date
            for (let index = 0; index < $(".log")[0].children.length; index++) {
                if ($(".log")[0].children[index].children[0].innerText.slice(0, 4) == this.d) {
                    this.staff.push($(".log")[0].children[index].children[4].innerText);
                    this.type.push($(".log")[0].children[index].children[1].innerText);
                }
            }
            document.getElementById('mode').value = '';
            this.b = true;
        },
        mode(){
            let mode =  document.getElementById('mode').value;
            let count = {};
            let number = [];

            switch(mode){
                case '1':
                    destroy();

                    // Count The Duplicates In An Array
                    this.staff.forEach(function(element) {
                        if (!count.hasOwnProperty(element)) { //or (!count[element])
                           count[element] = 1;
                        } else {
                           count[element]++;
                        }
                    });

                    this.staff = [];
                    
                    for (const key in count) {
                        this.staff.push(key);
                        number.push(count[key]);
                    }

                    this.b = !this.b;

                    // console.log(number);
                    // console.log(this.staff);

                    title = 'Laporan ' + this.d + ' Audit (Juruaudit)';
                    this.bar_graph(title, number);
                    break
                case '2':
                    destroy();

                    // Count The Duplicates In An Array
                    this.type.forEach(function(element) {
                        if (!count.hasOwnProperty(element)) { //or (!count[element])
                            count[element] = 1;
                        } else {
                            count[element]++;
                        }
                    });

                    this.type = [];
                    
                    for (const key in count) {
                        this.type.push(key);
                        number.push(count[key]);
                    }

                    this.b = !this.b;

                    // console.log(number);
                    // console.log(this.staff);

                    title = 'Laporan ' + this.d + ' Audit (Jenis Audit)';
                    this.pie_chart(title, number);
                    break
                default:
                    break;
            }
        },
        bar_graph(title, number){
            // Chart JS start here
            let myChart = document.getElementById('myChart').getContext('2d');
            window.massPopChart = new Chart(myChart, {
                type: 'bar', //bar, horizontalBar, pie, Line, doughnut, radar, polarArea
                data: {
                    labels: this.staff,
                    datasets: [{
                    axis: 'y',
                    label: '',
                    data: number,
                    fill: false,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(201, 203, 207, 0.2)'
                    ],
                    borderColor: [
                        'rgb(255, 99, 132)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
                        'rgb(201, 203, 207)'
                    ],
                    borderWidth: 1
                    }]
                },
                options: {
                    indexAxis: 'y',
                    scales:{
                        y:{
                            beginAtZero: true,
                        },
                    },
                    plugins:{
                        title:{
                            display:true,
                            text:title,
                            font:{size:25,},
                        },
                        legend:{
                            display:false,
                        },
                    },
                    responsive:true,
                    maintainAspectRatio:true,
                },
            });
        },
        pie_chart(title, number){
            // Chart JS start here
            let myChart = document.getElementById('myChart').getContext('2d');
            window.massPopChart = new Chart(myChart, {
                type: 'pie', //bar, horizontalBar, pie, Line, doughnut, radar, polarArea
                data: {
                    labels: this.type,
                      datasets: [{
                        label: this.type,
                        data: number,
                        backgroundColor: [
                          'rgb(255, 99, 132)',
                          'rgb(54, 162, 235)',
                          'rgb(255, 205, 86)'
                        ],
                        hoverOffset: 4
                      }]
                },
                options: {
                    plugins:{
                        title:{
                            display:true,
                            text:title,
                            font:{size:25,},
                        },
                        legend:{
                            display:true,
                        },
                    },
                    responsive:true,
                    maintainAspectRatio:true,
                },
            });
        },
        toggle(){
            this.a = !this.a;
        },
    }
})