// Create App
const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data(){
        return {
            a:false,
            plan: '',
            type: '',
            pengauditan: '',
            elemen: '',
            indicator: '',
            s: '',
            auditor: '',
            from:'',
            to:'',
            att: '',
            risk:'',
            Kebarangkalian:'',
            Impak:'',
            total:'',
            level:'',
            criteria:[],
            status:[],
        }
    },
    mounted: function() {
        // Calls the method before page loads
        this.password();
        this.getData();
        this.getDataPlan();
    },
    methods:{
        OnSubmit(){
            if (this.$refs.code.value != '') {
                this.$refs.form.submit();
            } else {
                alert('Sila isikan Kod.')
            }
            
        },
        getData(){
            this.plan = document.getElementById(this.$refs.code.value).cells[1].innerHTML;
            this.type = document.getElementById(this.$refs.code.value).cells[2].innerHTML;
            this.pengauditan = document.getElementById(this.$refs.code.value).cells[3].innerHTML;
            this.elemen = document.getElementById(this.$refs.code.value).cells[4].innerHTML;
            this.s = document.getElementById(this.$refs.code.value).cells[5].innerHTML;
            this.auditor = document.getElementById(this.$refs.code.value).cells[6].innerHTML;
            this.from = document.getElementById(this.$refs.code.value).cells[7].innerHTML;
            this.to = document.getElementById(this.$refs.code.value).cells[8].innerHTML;
            this.att = document.getElementById(this.$refs.code.value).cells[9].innerHTML;
        },
        getDataPlan(){
            this.department = document.getElementById(this.$refs.code.value).cells[6].innerHTML;
            this.auditor = document.getElementById(this.$refs.code.value).cells[7].innerHTML;
            this.from = document.getElementById(this.$refs.code.value).cells[8].innerHTML;
            this.to = document.getElementById(this.$refs.code.value).cells[9].innerHTML;
        },
        selectPerancangan(){
            for (let i = 0; i < document.getElementsByName('plan')[0].length; i++) {
                for (let j = 0; j < document.getElementsByName('type')[0].length; j++) {
                    if (document.getElementsByName('plan')[0][i].value == this.$refs.plan.value) {
                        if (document.getElementsByName('plan')[0][i].className == document.getElementsByName('type')[0][j].value) {
                            document.getElementsByName('type')[0][j].hidden = false;
                            document.getElementsByName('type')[0][j].selected = true;
                        } else {
                            document.getElementsByName('type')[0][j].hidden = true;
                        }
                    }
                }
            }
            this.type = '';
            this.pengauditan = '';
            this.selectJenis();
        },
        selectJenis(){
            for (let i = 0; i < document.getElementsByName('type')[0].length; i++) {
                for (let j = 0; j < document.getElementsByName('pengauditan')[0].length; j++) {
                    if (document.getElementsByName('type')[0][i].value == this.$refs.type.value) {
                        if (document.getElementsByName('type')[0][i].id == document.getElementsByName('pengauditan')[0][j].id) {
                            document.getElementsByName('pengauditan')[0][j].hidden = false;
                            document.getElementsByName('pengauditan')[0][j].selected = true;
                        } else {
                            document.getElementsByName('pengauditan')[0][j].hidden = true;
                        }
                    }
                }
            }
            this.selectPP();
            
        },
        selectPP(){
            let num = 0;

            for (let i = 0; i < document.getElementsByName('pengauditan')[0].length; i++) {
                if (document.getElementsByName('pengauditan')[0].children[i].className == this.$refs.type.value) {
                    num++;
                    document.getElementsByName('pengauditan')[0][i].selected = true;
                    document.getElementsByName('pengauditan')[0][i].hidden = false;
                } else {
                    document.getElementsByName('pengauditan')[0][i].hidden = true;
                }
            }

            if (num == 0) {
                for (let i = 0; i < document.getElementsByName('pengauditan')[0].length; i++) {
                    document.getElementsByName('pengauditan')[0][i].selected = false;
                    this.$refs.pengauditan.value = '';
                }
            }
        },
        searchDate(){
            let counter = document.getElementsByClassName('log').length;
            
            for (let i = 0; i < counter; i++) {
                if (document.getElementsByClassName('log')[i].outerText.substr(0, 4) == this.date) {
                    document.getElementsByClassName('log')[i].hidden = false;
                } else {
                    document.getElementsByClassName('log')[i].hidden = true;
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
        selectKriteria(){
            let senaraiSemak = document.getElementById('senaraiSemak').value;
            let scripts = ``;
            this.criteria = document.getElementsByClassName(senaraiSemak)[0].children[2].innerHTML.split(',')

            for (let i = 1; i <= document.getElementsByClassName('Kriteria')[0].children.length; i++) {
                if (document.getElementsByClassName('Kriteria')[0].children.length == i) {
                    document.getElementsByClassName('Kriteria')[0].children[i-1].children[0].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[0].innerHTML;
                    document.getElementsByClassName('Kriteria')[0].children[i-1].children[1].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[1].innerHTML;
                    for (let i = 0; i < this.criteria.length; i++) {
                        scripts += `<li>${(this.criteria[i])}</li>`;
                    }
                    document.getElementsByClassName('Kriteria')[0].children[i-1].children[2].outerHTML = `<td style="text-align: justify;"><ol>${(scripts)}</ol></td>`;
                    document.getElementsByClassName('Kriteria')[0].children[i-1].children[2].children[0].style.display = 'none';
                }
            }
            this.a = true;
            this.toggle();
        },
        addKriteria(){
            let counter = document.getElementsByClassName('Kriteria')[0].childNodes.length;

            const row = document.createElement("tr");
            const data = `<td></td><td></td><td></td><td><input type="radio" name="status ${(counter+1)}" id="yes" value="yes"><label for="yes">Ya</label><input type="radio" name="status ${(counter+1)}" id="no" value="no"><label for="no">Tidak</label></td></tr>`;
            row.id = `Kriteria ${(counter+1)}`;
            row.innerHTML = data;
            document.getElementsByClassName('Kriteria')[0].appendChild(row);
        },
        reset(){
            let id = document.getElementsByClassName('Kriteria')[0].children.length;
            let element = document.getElementById("Kriteria "+ id);

            element.parentNode.removeChild(element);
        },
        getStatus(){
            for (let i = 0; i < document.getElementsByClassName('Kriteria')[0].children.length; i++) {
                this.criteria[i] = document.getElementsByClassName('Kriteria')[0].children[i].children[0].innerText;

                if (document.getElementsByClassName('Kriteria')[0].children[i].children[3].childNodes[0].checked == true) {
                    this.status[i] = 'yes';
                } else {
                    this.status[i] = 'no';
                }
            }

            this.$refs.criteria.value = this.criteria;
            this.$refs.status.value = this.status;
            this.OnSubmit();
        },
        toggle(){
            this.a = !this.a;
            
            for (let i = 0; i < document.getElementsByClassName('Kriteria')[0].children.length; i++) {
                if (this.a == true) {
                    document.getElementsByClassName('Kriteria')[0].children[i].children[2].children[0].style.display = 'block';
                } else {
                    document.getElementsByClassName('Kriteria')[0].children[i].children[2].children[0].style.display = 'none';
                }
            }
        },
        password(){
            let passcode = prompt("Please enter password:", "");
            if (passcode == null || passcode == "" || passcode != 'auditor') {
                alert('You are not allow to proceed without password.');
                window.history.back();
            }
        },
    }
})