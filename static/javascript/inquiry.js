// Create App
const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data(){
        return {
            a:false,
            num:0,
            plan: '',
            type: '',
            element: '',
            elemen: '',
            subIndicator: '',
            auditor: '',
            date:'',
            att: '',
            risk:'',
            Kebarangkalian:'',
            Impak:'',
            total:'',
            level:'',
            status:[],
            criteria:[],
            catatan:[],
        }
    },
    mounted: function() {
        // Calls the method before page loads
        this.password();
        this.getData();
        this.getStatus();
    },
    methods:{
        OnSubmit(){
            for (let i = 0; i < document.getElementsByClassName('Kriteria')[0].children.length; i++) {
                this.criteria[i] = document.getElementsByClassName('Kriteria')[0].children[i].children[0].innerText + '*';
                this.catatan[i] = document.getElementsByClassName('Kriteria')[0].children[i].children[4].children[0].value + '*';

                if (document.getElementsByClassName('Kriteria')[0].children[i].children[3].childNodes[0].checked == true) {
                    this.status[i] = 'yes';
                } else {
                    this.status[i] = 'no';
                }
            }
            this.$refs.criteria.value = this.criteria;
            this.$refs.status.value = this.status;
            this.$refs.catatan.value = this.catatan;
            this.$refs.form.submit();
        },
        getData(){
            this.plan = document.getElementById(this.$refs.code.value).cells[1].innerHTML;
            this.type = document.getElementById(this.$refs.code.value).cells[2].innerHTML;
            this.element = document.getElementById(this.$refs.code.value).cells[3].innerHTML;
            this.elemen = document.getElementById(this.$refs.code.value).cells[4].innerHTML;
            this.subIndicator = document.getElementById(this.$refs.code.value).cells[5].innerHTML;
            this.auditor = document.getElementById(this.$refs.code.value).cells[6].innerHTML;
            this.criteria = document.getElementById(this.$refs.code.value).cells[7].innerHTML;
            this.status = document.getElementById(this.$refs.code.value).cells[8].innerHTML;
        },
        getNum(num){
            this.num = num;
            // alert('Sila pilih Senarai Semak '+num);
        },
        selectKriteria(){
            let senaraiSemak = document.getElementById('senaraiSemak').value;
            let scripts = ``;
            this.criteria = document.getElementsByClassName(senaraiSemak)[0].children[2].innerHTML.split(',')

            switch (this.num) {
                case 1:
                    document.getElementsByClassName('Kriteria')[0].children[0].children[0].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[0].innerHTML;
                    document.getElementsByClassName('Kriteria')[0].children[0].children[1].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[1].innerHTML;
                    for (let i = 0; i < this.criteria.length; i++) {
                        scripts += `<li>${(this.criteria[0])}</li>`;
                    
                        document.getElementsByClassName('Kriteria')[0].children[0].children[2].outerHTML = `<td style="text-align: justify;"><ol>${(scripts)}</ol></td>`;
                        document.getElementsByClassName('Kriteria')[0].children[0].children[2].children[0].style.display = 'none';
                    }
                    break;
                case 2:
                    document.getElementsByClassName('Kriteria')[0].children[1].children[0].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[0].innerHTML;
                    document.getElementsByClassName('Kriteria')[0].children[1].children[1].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[1].innerHTML;
                    for (let i = 0; i < this.criteria.length; i++) {
                        scripts += `<li>${(this.criteria[0])}</li>`;
                    
                        document.getElementsByClassName('Kriteria')[0].children[1].children[2].outerHTML = `<td style="text-align: justify;"><ol>${(scripts)}</ol></td>`;
                        document.getElementsByClassName('Kriteria')[0].children[1].children[2].children[0].style.display = 'none';
                    }
                    break;
                case 3:
                    document.getElementsByClassName('Kriteria')[0].children[2].children[0].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[0].innerHTML;
                    document.getElementsByClassName('Kriteria')[0].children[2].children[1].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[1].innerHTML;
                    for (let i = 0; i < this.criteria.length; i++) {
                        scripts += `<li>${(this.criteria[0])}</li>`;
                    
                        document.getElementsByClassName('Kriteria')[0].children[2].children[2].outerHTML = `<td style="text-align: justify;"><ol>${(scripts)}</ol></td>`;
                        document.getElementsByClassName('Kriteria')[0].children[2].children[2].children[0].style.display = 'none';
                    }
                    break;
                case 4:
                    document.getElementsByClassName('Kriteria')[0].children[3].children[0].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[0].innerHTML;
                    document.getElementsByClassName('Kriteria')[0].children[3].children[1].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[1].innerHTML;
                    for (let i = 0; i < this.criteria.length; i++) {
                        scripts += `<li>${(this.criteria[0])}</li>`;
                    
                        document.getElementsByClassName('Kriteria')[0].children[3].children[2].outerHTML = `<td style="text-align: justify;"><ol>${(scripts)}</ol></td>`;
                        document.getElementsByClassName('Kriteria')[0].children[3].children[2].children[0].style.display = 'none';
                    }
                    break;
                case 5:
                    document.getElementsByClassName('Kriteria')[0].children[4].children[0].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[0].innerHTML;
                    document.getElementsByClassName('Kriteria')[0].children[4].children[1].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[1].innerHTML;
                    for (let i = 0; i < this.criteria.length; i++) {
                        scripts += `<li>${(this.criteria[0])}</li>`;
                    
                        document.getElementsByClassName('Kriteria')[0].children[4].children[2].outerHTML = `<td style="text-align: justify;"><ol>${(scripts)}</ol></td>`;
                        document.getElementsByClassName('Kriteria')[0].children[4].children[2].children[0].style.display = 'none';
                    }
                    break;
                case 6:
                    document.getElementsByClassName('Kriteria')[0].children[5].children[0].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[0].innerHTML;
                    document.getElementsByClassName('Kriteria')[0].children[5].children[1].innerHTML = document.getElementsByClassName(senaraiSemak)[0].children[1].innerHTML;
                    for (let i = 0; i < this.criteria.length; i++) {
                        scripts += `<li>${(this.criteria[0])}</li>`;
                    
                        document.getElementsByClassName('Kriteria')[0].children[5].children[2].outerHTML = `<td style="text-align: justify;"><ol>${(scripts)}</ol></td>`;
                        document.getElementsByClassName('Kriteria')[0].children[5].children[2].children[0].style.display = 'none';
                    }
                    break;
                default:
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
                    break;
            }

            this.a = true;
            this.toggle();
        },
        addKriteria(){
            let counter = document.getElementsByClassName('Kriteria')[0].childNodes.length;

            const row = document.createElement("tr");
            const data = `<td></td><td style="width: 5%;"></td><td></td><td><input type="radio" name="status ${(counter+1)}" id="yes" value="yes"><label for="yes">Ya</label><input type="radio" name="status ${(counter+1)}" id="no" value="no"><label for="no">Tidak</label></td><td><input type="text"></td></tr>`;
            row.id = `Kriteria ${(counter+1)}`;
            row.innerHTML = data;
            document.getElementsByClassName('Kriteria')[0].appendChild(row);
        },
        reset(){
            document.getElementById('Kriteria 1').innerHTML = `<td style="cursor:pointer;"></td>
            <td style="width: 5%;"></td>
            <td></td>
            <td>
                <input type="radio" name="status 1" id="yes" value="yes">
                <label for="yes">Ya</label>
                <input type="radio" name="status 1" id="no" value="no">
                <label for="no">Tidak</label>
            </td>
            <td><input type="text"></td>
            <td><a href="https://1drv.ms/x/s!AlYqlCxLzsXahBTC1FoGkL2Nttyg?e=X3sC5D" target="_blank">Kriteria 1</a></td>`;
            document.getElementById('Kriteria 2').innerHTML = `                <td style="cursor:pointer;"></td>
            <td style="width: 5%;"></td>
            <td></td>
            <td>
                <input type="radio" name="status 2" id="yes" value="yes">
                <label for="yes">Ya</label>
                <input type="radio" name="status 2" id="no" value="no">
                <label for="no">Tidak</label>
            </td>
            <td><input type="text"></td>
            <td><a href="https://1drv.ms/x/s!AlYqlCxLzsXahBTC1FoGkL2Nttyg?e=X3sC5D" target="_blank">Kriteria 2</a></td>`;
            document.getElementById('Kriteria 3').innerHTML = `<td style="cursor:pointer;"></td>
            <td style="width: 5%;"></td>
            <td></td>
            <td>
                <input type="radio" name="status 3" id="yes" value="yes">
                <label for="yes">Ya</label>
                <input type="radio" name="status 3" id="no" value="no">
                <label for="no">Tidak</label>
            </td>
            <td><input type="text"></td>
            <td><a href="https://1drv.ms/x/s!AlYqlCxLzsXahBb30G7uMY64Pyuz?e=HbOsSq" target="_blank">Kriteria 3</a></td>`;
            document.getElementById('Kriteria 4').innerHTML = `<td style="cursor:pointer;"></td>
            <td style="width: 5%;"></td>
            <td></td>
            <td>
                <input type="radio" name="status 4" id="yes" value="yes">
                <label for="yes">Ya</label>
                <input type="radio" name="status 4" id="no" value="no">
                <label for="no">Tidak</label>
            </td>
            <td><input type="text"></td>
            <td><a href="https://1drv.ms/x/s!AlYqlCxLzsXahBi461dMuhzZMrfo?e=HS6WMI" target="_blank">Kriteria 4</a></td>`;
            document.getElementById('Kriteria 5').innerHTML = `<td style="cursor:pointer;"></td>
            <td style="width: 5%;"></td>
            <td></td>
            <td>
                <input type="radio" name="status 5" id="yes" value="yes">
                <label for="yes">Ya</label>
                <input type="radio" name="status 5" id="no" value="no">
                <label for="no">Tidak</label>
            </td>
            <td><input type="text"></td>
            <td><a href="https://1drv.ms/x/s!AlYqlCxLzsXahBpz_aW-dCEMDPNE?e=Ablas3" target="_blank">Kriteria 5</a></td>`;
            document.getElementById('Kriteria 6').innerHTML = `<td style="cursor:pointer;"></td>
            <td style="width: 5%;"></td>
            <td></td>
            <td>
                <input type="radio" name="status 6" id="yes" value="yes">
                <label for="yes">Ya</label>
                <input type="radio" name="status 6" id="no" value="no">
                <label for="no">Tidak</label>
            </td>
            <td><input type="text"></td>
            <td><a href="https://1drv.ms/x/s!AlYqlCxLzsXahBweGjj6v8bROd2w?e=kmbSZc" target="_blank">Kriteria 6</a></td>`;
        },
        getStatus(){
            this.criteria = this.criteria.split("*");
            this.criteria.pop();
            this.status = this.status.split(",");

            for (let index = 1; index < this.criteria.length; index++) {
                this.criteria[index] = this.criteria[index].slice(1);
            }

            console.log(this.criteria);

            for (let i = 0; i < this.status.length; i++) {
                let prosedur = document.getElementsByClassName(this.criteria[i])[0].children[2].innerText.split(',');
                let scripts = ``;
                if (this.criteria[i] == document.getElementsByClassName(this.criteria[i])[0].children[0].innerText) {
                    document.getElementsByClassName('Kriteria')[0].children[i].children[0].innerText = this.criteria[i];
                    document.getElementsByClassName('Kriteria')[0].children[i].children[1].innerText = document.getElementsByClassName(this.criteria[i])[0].children[1].innerHTML;

                    for (let k = 0; k < prosedur.length; k++) {
                        scripts += `<li>${(prosedur[k])}</li>`;
                    }
                    document.getElementsByClassName('Kriteria')[0].children[i].children[2].outerHTML = `<td><ol>${(scripts)}</ol></td>`;
                    document.getElementsByClassName('Kriteria')[0].children[i].children[2].children[0].style.display = 'none';
                }
                
                if (this.status[i] == 'yes') {
                    document.getElementsByClassName('Kriteria')[0].children[i].children[3].childNodes[0].checked = true;
                } else {
                    document.getElementsByClassName('Kriteria')[0].children[i].children[3].childNodes[2].checked = true;
                }
            }
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