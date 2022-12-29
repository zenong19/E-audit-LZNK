// Create App
const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data(){
        return {
            info_r:{},
            info_e:{},
            info_i:{},
            info_s:{},
            jenis:[],
            risiko:'',
            elemen:'',
            indikator:'',
            subIndikator:'',
            Kebarangkalian:'',
            Impak:'',
            total:'',
            level:'',
        }
    },
    mounted: function() {
        // Calls the method before page loads
        this.getData();
        this.selectJenis();
    },
    methods:{
        OnSubmit(){
            this.$refs.form.submit();
        },
        getData(){
            const alphabet = ['r', 'e', 'i', 's']
            alphabet.forEach(element => {
                let counter = document.getElementsByClassName(element).length;
                switch (element) {
                    case 'r':
                        for (let index = 1; index <= counter; index++) {
                            this.jenis.push(document.getElementById("r"+index).innerHTML.split(":")[0]);
                            this.info_r[document.getElementById("r"+index).innerHTML.split(":")[0]] = document.getElementById("r"+index).innerHTML.split(":")[1];
                        }
                        break;
                    case 'e':
                        for (let index = 1; index <= counter; index++) {
                            this.info_e[document.getElementById('e'+index).innerHTML.split(":")[0]] = document.getElementById('e'+index).innerHTML.split(":")[1];
                        }
                        break;
                    case 'i':
                        for (let index = 1; index <= counter; index++) {
                            this.info_i[document.getElementById('i'+index).innerHTML.split(":")[0]] = document.getElementById('i'+index).innerHTML.split(":")[1];
                        }
                        break;
                    case 's':
                        for (let index = 1; index <= counter; index++) {
                            this.info_s[document.getElementById('s'+index).innerHTML.split(":")[0]] = document.getElementById('s'+index).innerHTML.split(":")[1];
                        }
                        break;
                    default:
                        break;
                }
            });
            console.log('Data updated based on selection');
        },
        selectJenis(){
            const alphabet = ['r', 'e', 'i', 's']
            alphabet.forEach(element => {
                switch (element) {
                    case 'r':
                        for (const key in this.info_r) {
                            if (this.$refs.type.value == key) {
                                r = this.info_r[key]
                                r = r.replace("[","").replace("]","").replace(/['']/g,"").split(",");
                                this.risiko = r;
                            }else{
                                r = this.info_r[Object.keys(this.info_r)[0]]
                                r = r.replace("[","").replace("]","").replace(/['']/g,"").split(",");
                                this.risiko = r;
                            }
                        }
                        break;
                    case 'e':
                        for (const key in this.info_e) {
                            if (this.$refs.type.value == key) {
                                e = this.info_e[key]
                                e = e.replace("[","").replace("]","").replace(/['']/g,"").split(",");
                                this.elemen = e;
                            }else{
                                e = this.info_e[Object.keys(this.info_e)[0]]
                                e = e.replace("[","").replace("]","").replace(/['']/g,"").split(",");
                                this.elemen = e;
                            }
                        }
                        break;
                    default:
                        break;
                }
            });
            
        },
        selectElemen(){
            for (const key in this.info_i) {
                if (this.$refs.element.value == key) {
                    i = this.info_i[key]
                    i = i.replace("[","").replace("]","").replace(/['']/g,"").split(",");
                    this.indikator = i;
                }else{
                    i = this.info_i[Object.keys(this.info_i)[0]]
                    i = i.replace("[","").replace("]","").replace(/['']/g,"").split(",");
                    this.indikator = i;
                }
            }
        },
        selectIndicator(){
            for (const key in this.info_s) {
                if (this.$refs.indicator.value == key) {
                    s = this.info_s[key]
                    s = s.replace("[","").replace("]","").replace(/['']/g,"").split(",");
                    this.subIndikator = s;
                }else{
                    s = this.info_s[Object.keys(this.info_s)[0]]
                    s = s.replace("[","").replace("]","").replace(/['']/g,"").split(",");
                    this.subIndikator = s;
                }
            }
        },
        score(){
            let total = this.Kebarangkalian * this.Impak;
            this.total = total;
            
            if (total >= 15) {
                this.level = 'Tinggi';
                document.getElementsByName('level')[0].style.backgroundColor = 'red';
            } else if(total >= 5) {
                this.level = 'Sederhana';
                document.getElementsByName('level')[0].style.backgroundColor = 'yellow';
            } else {
                this.level = 'Rendah';
                document.getElementsByName('level')[0].style.backgroundColor = 'green';
            }
        },
        getKebarangkalian(){
            this.Kebarangkalian = this.$refs.Kebarangkalian.value;
            this.score();
        },
        getImpak(){
            this.Impak = this.$refs.Impak.value;
            this.score();
        },
    },
})