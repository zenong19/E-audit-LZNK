// Create App
const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data(){
        return {
            a:true,
            d:false,
            code:'',
            type:'',
            programme:'',
            pp:'',
            element:'',
            indicator:'',
            subIndicator:'',
            criteria:'',
            mark:'',
            prosedur:[],
            department:'',
            outcome:'',
            evidence:'',
            risk:'',
            staff:'',
            nama:'',
            position:'',
            remark:'',
            date:'',
        }
    },
    methods:{
        checkDatabase(){
            // Empty database. Save new data.
            if (document.getElementsByClassName('kod').length == 0) {
                console.log('Empty database', document.getElementsByClassName('kod').length);
                // To make sure code is filled
                if (this.code != "") {
                    this.OnSubmit('save');
                } else {
                    alert("Kod must be filled out");
                }
            } 
            // Check duplication.
            else {
                let text = "Kod telah ada dalam database. Adakah anda ingin kemaskini data tersebut?";
                let num = 0;
                for (let index = 0; index < document.getElementsByClassName('kod').length; index++) {
                    const element = document.getElementsByClassName('kod')[index].children[1].id;
                    if (element == this.code) {
                        num++;
                    }
                }
                if (num != 0) {
                    console.log(text);
                    if (confirm(text) == true) {
                        this.OnSubmit('save');
                    }
                } else {
                    // To make sure code is filled
                    if (this.code != "") {
                        this.OnSubmit('save');
                    } else {
                        alert("Kod must be filled out");
                    }
                }
            }
        },
        OnSubmit(key){
            document.getElementById('mode').value = key;
            this.$refs.form.submit();
        },
        OnDelete(key){
            document.getElementById('mode').value = key;
            this.$refs.form.submit();
        },
        toggle(){
            this.a = !this.a;
        },
        reset(){
            document.getElementById("code").readOnly = false;
            this.a = false;
            this.d = false;
            this.code = '';
            this.type = '';
            this.programme = '';
            this.pp = '';
            this.element = '';
            this.indicator = '';
            this.subIndicator = '';
            this.criteria = '';
            this.mark = '';
            this.prosedur = [];
            this.department = '';
            this.outcome = '';
            this.evidence = '';
            this.risk = '';
            this.staff = '';
            this.nama = '';
            this.position = '';
            this.remark = '';
            this.date = '';

            if (document.getElementsByClassName('Prosedur')[0].children.length > 1) {
                for (let index = 0; index < document.getElementsByClassName('Prosedur')[0].children.length; index++) {
                    this.minus();
                }
            }

            document.getElementsByClassName('Prosedur')[0].children[0].innerHTML = `<tr id="Prosedur 1"><td>1</td><td><textarea name="Prosedur 1" cols="30" rows="5"></textarea></td></tr>`;
        },
        OnEdit_Jenis_Audit(code,type){
            document.getElementById("code").readOnly = true;
            this.code = code;
            this.type = type;
            this.d = true;
        },
        OnEdit_Perancangan_Audit(code,programme,type,date){
            document.getElementById("code").readOnly = true;
            this.code = code;
            this.programme = programme;
            this.type = type;
            this.date = date;
            this.d = true;
        },
        OnEdit_Program_Pengauditan(code,pp,type){
            document.getElementById("code").readOnly = true;
            this.code = code;
            this.pp = pp;
            this.type = type;
            this.d = true;
        },
        OnEdit_Elemen_Kawalan(code,element,pengauditan){
            document.getElementById("code").readOnly = true;
            this.code = code;
            this.element = element;
            this.pp = pengauditan;
            this.d = true;
        },
        OnEdit_Indikator(code,indicator,element){
            document.getElementById("code").readOnly = true;
            this.code = code;
            this.indicator = indicator;
            this.element = element;
            this.d = true;
        },
        OnEdit_Sub_Indikator(code,subIndicator,indicator){
            document.getElementById("code").readOnly = true;
            this.code = code;
            this.subIndicator = subIndicator;
            this.indicator = indicator;
            this.d = true;
        },
        OnEdit_Senarai_Semak(code,criteria,mark,subIndicator,prosedur){
            this.reset();
            
            document.getElementById("code").readOnly = true;
            this.code = code;
            this.criteria = criteria;
            this.mark = mark;
            this.subIndicator = subIndicator;
            this.d = true;
            this.prosedur = prosedur.split(",");

            for (let index = 1; index < this.prosedur.length; index++) {
                this.addProsedur();
            }
            for (let index = 1; index < this.prosedur.length+1; index++) {
                document.getElementsByName('Prosedur '+ index)[0].value = this.prosedur[index-1];
            }
        },
        OnEdit_Jabatan(code,department){
            document.getElementById("code").readOnly = true;
            this.code = code;
            this.department = department;
            this.d = true;
        },
        OnEdit_Penemuan(code,outcome){
            document.getElementById("code").readOnly = true;
            this.code = code;
            this.outcome = outcome;
            this.d = true;
        },
        OnEdit_Jenis_Bukti(code,evidence){
            document.getElementById("code").readOnly = true;
            this.code = code;
            this.evidence = evidence;
            this.d = true;
        },
        OnEdit_Penilaian_Risiko(code,risk,type){
            document.getElementById("code").readOnly = true;
            this.code = code;
            this.risk = risk;
            this.type = type;
            this.d = true;
        },
        OnEdit_Team(staff,nama,position,date){
            document.getElementById("code").readOnly = true;
            this.code = staff;
            this.nama = nama;
            this.position = position;
            this.date = date;
            this.d = true;
        },
        OnEdit_History(code,date,position,staff,programme,pp,indicator,subIndicator,outcome,remark){
            document.getElementById("code").readOnly = true;
            this.code = code;
            this.staff = staff;
            this.position = position;
            this.date = date;
            this.programme = programme;
            this.pp = pp;
            this.indicator = indicator;
            this.subIndicator = subIndicator;
            this.outcome = outcome;
            this.remark = remark;
            this.d = true;
        },
        addProsedur(){
            let counter = document.getElementsByClassName('Prosedur')[0].childNodes.length;

            const row = document.createElement("tr");
            const data = `<td>${(counter+1)}</td><td><textarea name="Prosedur ${(counter+1)}" cols="30" rows="5"></textarea></td></tr>`;
            row.id = `Prosedur ${(counter+1)}`;
            row.innerHTML = data;
            document.getElementsByClassName('Prosedur')[0].appendChild(row);
        },
        minus(){
            let id = document.getElementsByClassName('Prosedur')[0].children.length;
            let element = document.getElementById("Prosedur "+ id);

            element.parentNode.removeChild(element);

            this.prosedur.pop();
        },
        getProsedur(){
            for (let i = 0; i < document.getElementsByClassName('Prosedur')[0].children.length; i++) {
                this.prosedur[i] = document.getElementsByClassName('Prosedur')[0].children[i].children[1].childNodes[0].value;
            }
            this.$refs.prosedur.value = this.prosedur;
            this.checkDatabase();
        },
    }
})