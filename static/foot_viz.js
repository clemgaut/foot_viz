function MatchEventViz(match_data, div_id) {

    if (typeof div_id === "undefined") {
        this.div = d3.select("body").append("div");
    }else{
        this.div = d3.select("#".concat(div_id));
    }
    this.data = match_data;

    this.plot = function(){
        console.log("Nothing for now !");
    };

}