class Songs {
    constructor(tableId, keySet = []) {
      this.table = document.getElementById(tableId);
      this.keySet = ["id", "title"];
    }
    
    getData(){
        fetch("/converter/get-videos")
        .then((response)=>response.json())
        .then((data)=>{
            this.deleteTable();
            for(let i = 0; i<data.length;i++){
                this.addRow(data[i]);
                console.log(data[i]);
            }
        })
    }
    addRow(data){
        let row = this.table.insertRow();
        for (let i = 0; i < this.keySet.length; i++) {
            let cell = row.insertCell();
            cell.innerHTML = data[this.keySet[i]];
          }
    }
    deleteTable() {
        while (this.table.rows.length > 1) {
          this.table.deleteRow(0);
        }
      }
    
   
}
export default Songs;