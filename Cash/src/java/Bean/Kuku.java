package Bean;


import entity.Cash;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;


public class Kuku implements Comparable<Kuku>{
    
    private String u1name;
    private String u2name;
    private String u1value;
    private String u2value;
    private Boolean record;
    private String value2c;     //value to compare
    private int oneOrTwo;
    private List<Cash> all;    

    public Kuku(String _u1n, String _u1y, String _u1m, String _u1d, String _u1h, String _u1mi,
            String _u2n, String _u2y, String _u2m, String _u2d, String _u2h, String _u2mi) throws ParseException {
       
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm"); 
        String _u1StringDate = "";
        String _u2StringDate = "";
        Date _u1Date;
        Date _u2Date;
        long _u1TDate = 0;
        long _u2TDate = 0;
                            
        this.u1name = _u1n;
        this.u2name = _u2n;      
        this.u1value = "";
        this.u2value = "";
        this.value2c = "";
        this.oneOrTwo = 0;
        
        if (Integer.valueOf(_u1d) == 0){
            this.u1value = "no data";
        } else {
            if (_u1m.length() == 1) _u1m = "0" + _u1m;
            if (_u1d.length() == 1) _u1d = "0" + _u1d;
            if (_u1mi.length() == 1) _u1mi = "0" + _u1mi;
            _u1StringDate = _u1y + "/" + _u1m + "/" + _u1d + " " + _u1h + ":" + _u1mi;            
            _u1Date = dateFormat.parse(_u1StringDate);
            _u1TDate = _u1Date.getTime()/1000;
        }
        
        if (Integer.valueOf(_u2d) == 0 ){
            this.u2value = "no data";
        } else {
            if (_u2m.length() == 1) _u2m = "0" + _u2m;
            if (_u2d.length() == 1) _u2d = "0" + _u2d;
            if (_u2mi.length() == 1) _u2mi = "0" + _u2mi;
            _u2StringDate = _u2y + "/" + _u2m + "/" + _u2d + " " + _u2h + ":" + _u2mi;                     
            _u2Date = dateFormat.parse(_u2StringDate);            
             _u2TDate = _u2Date.getTime()/1000;
         }                                                                               
        
        if (this.u1value.compareTo("no data") == 0){
            if (this.u2value.compareTo("no data") != 0){
                this.u2value = _u2StringDate;
            }
        }
        
        if (this.u2value.compareTo("no data") == 0){
            if (this.u1value.compareTo("no data") != 0){
                this.u1value = _u1StringDate;
            }
        }
        
        if (this.u1value.compareTo("no data") != 0 && this.u2value.compareTo("no data") != 0) {
            if (_u1TDate - _u2TDate < 0){
                this.u1value = _u1StringDate;
                long _hours = (_u2TDate - _u1TDate) / 3600;
                String _minutes = String.valueOf(((_u2TDate - _u1TDate) % 3600) / 60);
                String _hoursStr = String.valueOf(_hours);
                if (Integer.parseInt(_minutes) < 10) _minutes = "0" + _minutes;
                if (Integer.parseInt(_hoursStr) < 10) _hoursStr = "0" + _hoursStr;
                this.u2value = "\u0394" + _hoursStr + ":"+ _minutes;
                this.value2c = String.valueOf( _hours * 60  + Integer.parseInt(_minutes));
                this.oneOrTwo = 2;
                
            } else if (_u1TDate - _u2TDate > 0){
                this.u2value = _u2StringDate;
                long _hours = (_u1TDate - _u2TDate) / 3600;
                String _minutes = String.valueOf(((_u1TDate - _u2TDate) % 3600) / 60);
                String _hoursStr = String.valueOf(_hours);
                if (Integer.parseInt(_hoursStr) < 10) _hoursStr = "0" + _hoursStr;
                if (Integer.parseInt(_minutes) < 10) _minutes = "0" + _minutes;
                this.u1value = "\u0394" + _hoursStr + ":" + _minutes;
                this.value2c = String.valueOf( _hours * 60  + Integer.parseInt(_minutes));
                this.oneOrTwo = 1;
                
            } else {
                this.u1value = _u1StringDate;
                this.u2value = _u2StringDate;
                this.value2c = "0";
            }        
        } else {
            this.value2c = "no data";
        }
    }

    public void setU1value(String u1value) {
        this.u1value = u1value;
    }

    public void setU2value(String u2value) {
        this.u2value = u2value;
    }


    public int getOneOrTwo() {
        return oneOrTwo;
    }

    public void setOneOrTwo(int oneOrTwo) {
        this.oneOrTwo = oneOrTwo;
    }
    
    public String getU1name(){
        return u1name;
    }

    public String getU1value() {
        return u1value;
    }

    public String getValue2c() {
        return value2c;
    }

    public String getU2name() {
        return u2name;
    }

    public String getU2value() {
        return u2value;
    }
    
    public Boolean getRecord() {
        return record;
    }

    public void setRecord(Boolean record) {
        this.record = record;
    }
        

    @Override
    public int compareTo(Kuku o) {       
        long _tValue2c;
        long _oValue2c;
        int rcVal = 0;
        
        if (this.getValue2c().compareTo("no data") != 0) 
            _tValue2c = Integer.valueOf(this.getValue2c());
        else
            _tValue2c = 0;
        if (o.getValue2c().compareTo("no data") != 0)            
            _oValue2c = Integer.valueOf(o.getValue2c());
        else
            _oValue2c = 0;

         if ( _tValue2c > _oValue2c)
            rcVal = 1;
        else if (_tValue2c < _oValue2c)
            rcVal = -1; 
                    
        return rcVal;
    }
}