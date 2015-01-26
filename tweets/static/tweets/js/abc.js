var PayRate = PayRate || {};
    
    PayRate.Scale = {
      "lt": "lt",
      "gt": "gt",
      "eq": "eq"
    };
    
    PayRate.makeScale = function(name, factor, id) {
      return {
        "name": name,
        "factor": factor,
        "id": id
      };
    };
    
    // Determines if 'Scale1' is greater than, less than or equal to 'Scale2'.
    PayRate.cmpSc = function(scale1, scale2) {
      if(scale1["id"] > scale2["id"])
        return PayRate.Scale.gt;
      if(scale1["id"] < scale2["id"])
        return PayRate.Scale.lt;
      return PayRate.eq;
    };
    
    // Determines the next scale in 'PayRate.Scales' based on
    // a scale 's', and a comparision value ('lt', 'gt)
    PayRate.nxtSc = function(s, ratio) {
      // If 'less than', then return the next larger scale.
      if(_.isEqual(ratio, PayRate.Scale["lt"]))
        return PayRate.Scales[s["id"] + 1];
      // If 'greater than', then return the next smaller scale.
      else if(_.isEqual(ratio, PayRate.Scale["gt"]))
        return PayRate.Scales[s["id"] - 1];
    }
    
    PayRate.Hour =  PayRate.makeScale("hour",  1, 0);
    PayRate.Day =   PayRate.makeScale("day",   8, 1);
    PayRate.Week =  PayRate.makeScale("week",  5, 2);
    PayRate.Month = PayRate.makeScale("month", 4, 3);
    PayRate.Year =  PayRate.makeScale("year", 12, 4);
    PayRate.Scales = [PayRate.Hour, PayRate.Day, PayRate.Week, PayRate.Month, PayRate.Year];
    
    PayRate.Pay = function(amount, scale) {
      this.amount = typeof(amount) !== "undefined" ? amount : 0;
      this.scale = typeof(scale) !== "undefined" ? scale : PayRate.Hour;
      return this;
    };
    
    // Get the factor, multiply or divide, then change the internal scale.
    PayRate.Pay.prototype.doOperation = function(newScale) {
      var res = this.getFactor(this.scale, newScale);
      
      if(_.isEqual(res["ratio"], PayRate.Scale["lt"]) === true) {
        // Divide.
        this.amount = this.amount * res["factor"];
      }
      else if(_.isEqual(res["ratio"], PayRate.Scale["gt"]) === true) {
        // Multiply.
        this.amount = this.amount / res["factor"];
      }
      this.scale = newScale;
    }
    
    PayRate.Pay.prototype.hour = function() {
      this.doOperation(PayRate.Hour);
      return this;
    }
    
    PayRate.Pay.prototype.day = function() {
      this.doOperation(PayRate.Day);
      return this;
    }
    
    PayRate.Pay.prototype.week = function() {
      this.doOperation(PayRate.Week);
      return this;
    }
    
    PayRate.Pay.prototype.month = function() {
      this.doOperation(PayRate.Month);
      return this;
    }
    
    PayRate.Pay.prototype.year = function() {
      this.doOperation(PayRate.Year);
      return this;
    }
    
    PayRate.Pay.prototype.getFactor = function(scale1, scale2) {
      // If scale is itself, return 1.
      if(_.isEqual(scale1, scale2))
        return 1;
      // Determine if 'Scale1' is less than or greater than 'Scale2'.
      var ratio = PayRate.cmpSc(scale1, scale2);
      //console.log("Ratio is " + ratio);
      
      // Collect the scale factors.
      var factor = [];
      for(var i = scale1; 
         _.isEqual(PayRate.cmpSc(i, scale2)) === false || _.isEqual(PayRate.cmpSc(i, scale2)) === true; 
         i = PayRate.nxtSc(i, ratio)) {
        
        // If it is the last loop, push only if descending.
        if(_.isEqual(PayRate.cmpSc(i, scale2)) === true) {
          if(_.isEqual(ratio, PayRate.Scale["gt"]) === false) {
            //console.log("Last loop. i is now " + i["name"] + "\n");
            factor.push(i["factor"]);
          }
          break;
        }
        
        //console.log("i is now " + i["name"] + "\n");
        // If the ratio is ascending, and the counter is the first scale.
        if(_.isEqual(ratio, PayRate.Scale["lt"]) === true && _.isEqual(i, scale1) === true)
          //console.log("Ratio Ascending, counter first scale");
          ;
        // If the ratio is descending, and the counter is the last scale.
        else if(_.isEqual(ratio, PayRate.Scale["gt"]) === true && _.isEqual(i, scale2) === true)
          //console.log("Ratio Descending, counter last scale");
          ;
        else 
          factor.push(i["factor"]);
      }
      
      // Reduce factors into a single value.
      factor = _.reduce(factor, function(a, b) {return a * b;}, 1);
      return {
        "factor": factor, 
        "ratio": ratio
      };
    };