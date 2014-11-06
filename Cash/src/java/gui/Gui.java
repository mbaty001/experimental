/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package gui;

import Bean.CashBean;
import Bean.Kuku;
import entity.Cash;
import entity.User;
import java.io.IOException;
import java.text.DecimalFormat;
import java.text.ParseException;
import java.util.*;
import javax.annotation.PostConstruct;
import javax.ejb.EJB;
import javax.faces.application.FacesMessage;
import javax.faces.bean.ApplicationScoped;
import javax.faces.bean.ManagedBean;
import javax.faces.context.FacesContext;
import org.primefaces.component.datatable.DataTable;
import org.primefaces.event.CellEditEvent;
import org.primefaces.model.chart.CartesianChartModel;  
import org.primefaces.model.chart.ChartSeries;  

/**
 *
 * @author mbaty001
 */
@ManagedBean
@ApplicationScoped
public class Gui {

    private final static int[] YEARS;
    private final static int[] MONTHS;
    private final static int[] MONTHS_FOR_NEW;    
    private final static int[] DAYS;
    private final static int[] DAYS_FOR_NEW;
    private final static int[] HOURS;
    private final static int[] MINUTES;
    private final static int cMonth;
    private final static int cDay;
    private final static String version="Cash v1.3 by mbaty001";
    
    private List<Kuku> allData;
    private List<Cash> allCash;
    private int newYear;
    private int newMonth;
    private String newUser;
    private int newUYear;
    private int newUMonth;
    private int newUDay;
    private int newUHour;
    private int newUMinute;
    private List<Integer> fullYears; // years with 12 entries
    private List<Integer> yearsForNew;
    private String validatedMY;
    private String validatedMYU;
    private String validatedData;
    private String stats;
    private CartesianChartModel cStatsModel; 
    private CartesianChartModel dStatsModel; 
    private CartesianChartModel tStatsModel; 
    private CartesianChartModel cOverallModel;
    private String cStatsRender;
    private String dStatsRender;
    private String tStatsRender;
    private String cOverallRender;
    private String cashAdvantage; // amount of cash earned by current leaded on bank's interests
    
    @EJB
    CashBean obj;   
    
    static {
        YEARS = new int[10];
        int _y = 2007;
        for(int j=0; j<10; j++){
            YEARS[j] = _y;
            _y++;
        }
     }
        
    static {
        cMonth = Calendar.getInstance().get(Calendar.MONTH) + 1;
        MONTHS_FOR_NEW = new int[12];
        MONTHS_FOR_NEW[0] = cMonth;
        int _m = 1;
        for (int i=1; i < 12; i++){
            if (_m == cMonth)
                _m++;
            MONTHS_FOR_NEW[i] = _m;
            _m++;
        }
    }
    
    static {
        MONTHS = new int[12];
        for (int i=0; i < 12; i++){
            MONTHS[i] = i+1;
        }
    }
    
    static {
        cDay = Calendar.getInstance().get(Calendar.DAY_OF_MONTH);      
        DAYS_FOR_NEW = new int[31];
        DAYS_FOR_NEW[0] = cDay;
        int _d = 1;
        for (int i=1; i<31; i++){
            if (_d == cDay)
                _d++;
            DAYS_FOR_NEW[i] = _d;
            _d++;
        }
    }
    
    static {
        DAYS = new int[31];
        for (int i=0; i<31; i++){
            DAYS[i] = i+1;
        }
    }
    
    static {
        HOURS = new int[24];
        for (int i=0; i<24; i++){
            HOURS[i] = i;
        }        
    }
    
    static {
        MINUTES = new int[60];
        for (int i=0; i<60; i++){
            MINUTES[i] = i;
        }        
    }
               
    public List<Cash> getKasa(){
        return this.allCash;    
    }
    
    public int[] getYears(){
        return YEARS;
    }

    public List<Integer> getYears_for_new() {
        return this.yearsForNew;
    }
    
    public int[] getMonths(){
        return MONTHS;
    }

    public int[] getMonths_for_new() {
        return MONTHS_FOR_NEW;
    }

    public int[] getDays(){
        return DAYS;
    }

    public int[] getDays_for_new() {
        return DAYS_FOR_NEW;
    }
    
    public int[] getHours(){
        return HOURS;
    }
    
    public int[] getMinutes(){
        return MINUTES;
    }
    
    public List<User> getUsers(){
        return obj.findAllUsers();
    }
    
    public List<String> getUserNames(){
        return obj.findAllUserNames();
    }
    
    public List<Kuku> getKuku(){
        return this.allData;
    }
    
    public int getNewYear(){
        return this.newYear;
    }

    public void setNewYear(int newYear) {
        this.newYear = newYear;
    }  
    
    public int getNewMonth() {
        return newMonth;
    }

    public void setNewMonth(int newMonth) {
        this.newMonth = newMonth;
    }

    public String getNewUser() {
        return newUser;
    }

    public void setNewUser(String newUser) {
        this.newUser = newUser;
    }

    public int getNewUDay() {
        return newUDay;
    }

    public void setNewUDay(int newUDay) {
        this.newUDay = newUDay;
    }

    public int getNewUHour() {
        return newUHour;
    }

    public void setNewUHour(int newUHour) {
        this.newUHour = newUHour;
    }

    public int getNewUMinute() {
        return newUMinute;
    }

    public void setNewUMinute(int newUMinute) {
        this.newUMinute = newUMinute;
    }

    public int getNewUMonth() {
        return newUMonth;
    }

    public void setNewUMonth(int newUMonth) {
        this.newUMonth = newUMonth;
    }

    public int getNewUYear() {
        return newUYear;
    }

    public void setNewUYear(int newUYear) {
        this.newUYear = newUYear;
    }

    public String getValidatedMY() {
        return validatedMY;
    }

    public void setValidatedMY(String validatedMY) {
        this.validatedMY = validatedMY;
    }

    public String getValidatedMYU() {
        return validatedMYU;
    }

    public void setValidatedMYU(String validatedMYU) {
        this.validatedMYU = validatedMYU;
    }

    public String getValidatedData() {
        return validatedData;
    }

    public void setValidatedData(String validatedData) {
        this.validatedData = validatedData;
    }
         
    public String getVersion(){
        return version;
    }

    public String getStats() {
        return stats;
    }

    public void setStats(String stats) {
        this.stats = stats;
    }

    public CartesianChartModel getcStatsModel() {
        return cStatsModel;
    }

    public void setcStatsModel(CartesianChartModel cStatsModel) {
        this.cStatsModel = cStatsModel;
    }

    public String getcStatsRender() {
        return cStatsRender;
    }

    public CartesianChartModel getdStatsModel() {
        return dStatsModel;
    }

    public void setdStatsModel(CartesianChartModel dStatsModel) {
        this.dStatsModel = dStatsModel;
    }

    public CartesianChartModel gettStatsModel() {
        return tStatsModel;
    }

    public void settStatsModel(CartesianChartModel tStatsModel) {
        this.tStatsModel = tStatsModel;
    }

    public CartesianChartModel getcOverallModel() {
        return cOverallModel;
    }

    public void setcOverallModel(CartesianChartModel cOverallModel) {
        this.cOverallModel = cOverallModel;
    }
        
    public void setcStatsRender(String cStatsRender) {
        this.cStatsRender = cStatsRender;
    }

    public String getdStatsRender() {
        return dStatsRender;
    }

    public void setdStatsRender(String dStatsRender) {
        this.dStatsRender = dStatsRender;
    }

    public String gettStatsRender() {
        return tStatsRender;
    }

    public void settStatsRender(String tStatsRender) {
        this.tStatsRender = tStatsRender;
    }

    public String getcOverallRender() {
        return cOverallRender;
    }

    public void setcOverallRender(String cOverallRender) {
        this.cOverallRender = cOverallRender;
    }

    public String getCashAdvantage() {
        return cashAdvantage;
    }

    public void setCashAdvantage(String cashAdvantage) {
        this.cashAdvantage = cashAdvantage;
    }
        
    @PostConstruct
    public void readAllData(){
        Integer _cYear;
        Integer _y = 2007;
        this.newYear = 0;
        this.yearsForNew = new ArrayList();
        ArrayList<Integer> noOfWins;
        HashMap _days = new HashMap<Integer, Integer>(); 
        HashMap _timeP = new HashMap<Integer, String>();
        HashMap _timeM = new HashMap<Integer, String>();
        Integer _current;
        ArrayList _daysKeys;
        ArrayList _timeKeysP;
        ArrayList _timeKeysM;
        ChartSeries _tempChart;
        String _t;
        Integer _minute;
        Integer _hour;
        String _addM;
        String _addH;
        int overall1 = 0;
        int overall2 = 0;
        DecimalFormat df = new DecimalFormat("#.##");
        
        try {
            this.allData = obj.setEverything();
            this.allCash = obj.findAll();
            
            /*
             * Competition cash statistics
             */
            noOfWins = obj.getNoOfWins(this.allData);
            this.cStatsModel = new CartesianChartModel();
            ChartSeries chartMichal = new ChartSeries();
            chartMichal.setLabel("Michal");
            chartMichal.set("How many times competitor got the cash first", noOfWins.get(1));  
            ChartSeries chartPrzemek = new ChartSeries();                        
            chartPrzemek.setLabel("Przemek");
            chartPrzemek.set("How many times competitor got the cash first", noOfWins.get(0)); 
            
            this.cStatsModel.addSeries(chartMichal);
            this.cStatsModel.addSeries(chartPrzemek);
            
            /*
             * Date cash statistics
             */
            this.dStatsModel = new CartesianChartModel();
            for (Cash c: this.allCash){
                if (_days.get(c.getU1day()) == null){
                    _current = 1;
                } else {
                    _current = Integer.parseInt(_days.get(c.getU1day()).toString()) + 1;
                }
               
                _days.put(Integer.parseInt(c.getU1day().toString()), _current);                        
            }
            _daysKeys = new ArrayList(_days.keySet());            
            Collections.sort(_daysKeys);

            for (Object _keyO: _daysKeys){           
               _tempChart = new ChartSeries();
               _tempChart.setLabel(_keyO.toString());
               _tempChart.set("Day of month when cash delivered statistics", (Number)_days.get(_keyO));
               this.dStatsModel.addSeries(_tempChart);
            }
            
            /*
             * Time cash statistics
             */
            this.tStatsModel = new CartesianChartModel();
            // Przemas
            for (Cash c: this.allCash){

                _minute = (c.getU1minute() / 30) * 30;
                _hour = c.getU1hour();

                if (_minute == 0 && _hour == 0)
                    continue;

                if (_minute < 10)
                    _addM = "0";
                else
                    _addM = "";
                
                if (_hour < 10)
                    _addH = "0";
                else
                    _addH = "";                                                                
                
                _t = _addH + _hour.toString() + ":" + _addM + _minute.toString();                
                
                if (_timeP.get(_t) == null){
                    _current = 1;
                } else {
                    _current = Integer.parseInt(_timeP.get(_t).toString()) + 1;
                }
                _timeP.put(_t, _current);
            }
            
            /*
             * Overall statistics
             */
            for (Kuku k: this.allData) {
                System.out.println("1or2: " + k.getOneOrTwo());
                System.out.println("v2c: " + k.getValue2c());
                if (k.getValue2c().compareTo("no data") != 0) {                   
                    if (k.getOneOrTwo() == 1) {
                        /*
                        * first guy got the cash later
                        */                    
                        overall1 -= Integer.valueOf(k.getValue2c());
                        overall2 += Integer.valueOf(k.getValue2c()); 
                    } else {
                        /*
                        * second guy got the cash later
                        */
                        overall1 += Integer.valueOf(k.getValue2c());
                        overall2 -= Integer.valueOf(k.getValue2c());                     
                    }
                }
            }
            
            this.cOverallModel = new CartesianChartModel();
            ChartSeries _chartMichal = new ChartSeries();
            _chartMichal.setLabel("Michal");
            _chartMichal.set("What is the overall advantage result (in hours)", overall2/60);  
            ChartSeries _chartPrzemek = new ChartSeries();                        
            _chartPrzemek.setLabel("Przemek");
            _chartPrzemek.set("What is the overall advantage result (in hours)", overall1/60); 
            
            /*
             * 10k salary, 5% banks's interest, 20% belka, 365 days, 24 hours 
             */
            this.setCashAdvantage( df.format((((12000 * 0.03 * 0.8) / 365 ) / 24 ) * Math.abs(overall1/60)));
            this.cOverallModel.addSeries(_chartMichal);
            this.cOverallModel.addSeries(_chartPrzemek);
            
            //Michal
            for (Cash c: this.allCash){
                _minute = (c.getU2minute() / 30) * 30;
                _hour = c.getU2hour();
                
                if (_minute == 0 && _hour == 0)
                    continue;
                
                if (_minute < 10)
                    _addM = "0";
                else
                    _addM = "";
                
                if (_hour < 10)
                    _addH = "0";
                else
                    _addH = "";                                                                
                
                _t = _addH + _hour.toString() + ":" + _addM + _minute.toString();

                if (_timeM.get(_t) == null){
                    _current = 1;
                } else {
                    _current = Integer.parseInt(_timeM.get(_t).toString()) + 1;
                }
                _timeM.put(_t, _current);
            }
            
            /*
             * Add lacking entries
             */
            for (Object _keyO : _timeP.keySet()){
                if (! _timeM.containsKey(_keyO)){
                    _timeM.put(_keyO, 0);
                }
            }

            for (Object _keyO : _timeM.keySet()){
                if (! _timeP.containsKey(_keyO)){
                    _timeP.put(_keyO, 0);
                }
            }
                
            _timeKeysP = new ArrayList(_timeP.keySet());
            Collections.sort(_timeKeysP);
            _timeKeysM = new ArrayList(_timeM.keySet());
            Collections.sort(_timeKeysM);
            
            _tempChart = new ChartSeries();
            _tempChart.setLabel("Przemek");
            for (Object _keyO : _timeKeysP){                               
                _tempChart.set(_keyO.toString(), (Number)_timeP.get(_keyO));                
            }
            this.tStatsModel.addSeries(_tempChart);

            _tempChart = new ChartSeries();
            _tempChart.setLabel("Michal");
            for (Object _keyO : _timeKeysM){ 
                _tempChart.set(_keyO.toString(), (Number)_timeM.get(_keyO));                
            }
            this.tStatsModel.addSeries(_tempChart);
            
            _cYear = Calendar.getInstance().get(Calendar.YEAR);
            this.fullYears= obj.findFullYears(); 
            if (! this.fullYears.contains(_cYear)){
                this.yearsForNew.add(_cYear);
            }
        
            int j=0;
            while (j < 10){
                if (! _y.equals(_cYear) && ! this.fullYears.contains(_y)){
                    this.yearsForNew.add(_y);
                    j++;
                }
                _y++;
            }
        } catch (ParseException e) {
            System.out.println(e.toString());
            this.allData = null;
            this.allCash = null;
            this.yearsForNew = null;
        }                       
    }
      
    public Gui() {
    }
    
    public void onCellEdit(CellEditEvent event) {
        Object oldValue = event.getOldValue();  
        Object newValue = event.getNewValue();
                         
        if(newValue != null && !newValue.equals(oldValue)) {  
            DataTable s = (DataTable) event.getSource();

            Cash c = (Cash) s.getRowData();
        
            System.out.println("C: " + c.toString());
            
            try {
                obj.saveCash(c);
                this.readAllData();
            } catch (Exception e) {
                System.out.println(e.toString());
            }
            
            System.out.println("C: " + c.toString());
            
            FacesMessage msg = new FacesMessage(FacesMessage.SEVERITY_INFO, "Cell Changed", "Old: " + oldValue + ", New:" + newValue);  
            FacesContext.getCurrentInstance().addMessage(null, msg);  
        }  
    } 
    
    public void addNewData(){
        
    }
    
    public void validateMY(){
        
        List <Cash> entryExists = obj.findByMonthYear(this.newMonth, this.newYear);
        System.out.println("validateMY: " + entryExists.toString());
        if (entryExists.isEmpty()){
            System.out.println("MY validated");
            this.setValidatedMY("true");
        } else {
            System.out.println("MY NOT validated");
            FacesMessage msg = new FacesMessage(FacesMessage.SEVERITY_ERROR, "Try again", this.newYear + "/" + this.newMonth + " entry already exists");  
            FacesContext.getCurrentInstance().addMessage(null, msg); 
            this.setValidatedMY("false");
            this.setValidatedMYU("false");
            this.setValidatedData("false");  
        }        
    }
    
    public void validateUser(){
        /*
         * So far does nothing. Maybe latter....         
         */
        this.setValidatedMYU("true");
    }
    
    public void validateData(){
        /*
         * So far does nothing. Maybe latter....         
         */
        this.setValidatedData("true");        
    }
    
    public String SaveData() {
        Cash _cash;
        User _user1;
        User _user2;
        User _user;
        
        FacesMessage msg = new FacesMessage(FacesMessage.SEVERITY_INFO, "Data saved successfully", "");
        FacesContext.getCurrentInstance().addMessage(null, msg);
        
        _user1 = obj.findUserByName("Przemek");      
        _user2 = obj.findUserByName("Michal"); 
        _user = obj.findUserByName(this.newUser);
        System.out.println("saveData");
        System.out.println("Year: " + this.newYear);
        System.out.println("Month: " + this.newMonth);
        System.out.println("User: " + this.newUser);
        System.out.println("User: " + _user.getId());
        System.out.println("User1 id: " + _user1.getId());
        System.out.println("User2 id: " + _user2.getId());
        System.out.println("User Y: " + this.newUYear);
        System.out.println("User M: " + this.newUMonth);
        System.out.println("User D: " + this.newUDay);
        System.out.println("User H: " + this.newUHour);
        System.out.println("User Mi: " + this.newUMinute);
        
        _cash = new Cash(this.newYear, this.newMonth);   
        _cash.setUser1(_user2);
        _cash.setUser2(_user1);
        if (_user.getId() == 1){
            _cash.setU1year(this.newUYear);
            _cash.setU1month(this.newUMonth);
            _cash.setU1day(this.newUDay);
            _cash.setU1hour(this.newUHour);
            _cash.setU1minute(this.newUMinute);
            _cash.setU2year(this.newYear);
            _cash.setU2month(this.newMonth);
            _cash.setU2day(0);
            _cash.setU2hour(0);
            _cash.setU2minute(0);
        } else {
            _cash.setU2year(this.newUYear);
            _cash.setU2month(this.newUMonth);
            _cash.setU2day(this.newUDay);
            _cash.setU2hour(this.newUHour);
            _cash.setU2minute(this.newUMinute);
            _cash.setU1year(this.newYear);
            _cash.setU1month(this.newMonth);
            _cash.setU1day(0);
            _cash.setU1hour(0);
            _cash.setU1minute(0);            
        }
        
        System.out.println("Cash: " + _cash.toString());
        obj.persistCash(_cash);
        
        this.readAllData();
        
        return "index.xhtml";
    }
    
    public void procesStats(){
        String _stats = this.getStats();
        String _statsFull = "";
        

        
        if( _stats.compareTo("cDate") == 0 ){
            _statsFull = "Cash Date";
             this.cStatsRender = "false";
             this.dStatsRender = "true";
             this.tStatsRender = "false";  
             this.cOverallRender = "false";
        } else if ( _stats.compareTo("cTime") == 0 ){
            _statsFull = "Cash Time";
             this.cStatsRender = "false";
             this.dStatsRender = "false";
             this.tStatsRender = "true";             
             this.cOverallRender = "false";
        } else if ( _stats.compareTo("cCompet") == 0 ){
             _statsFull = "Cash Competition";
             this.cStatsRender = "true";
             this.dStatsRender = "false";
             this.tStatsRender = "false";  
             this.cOverallRender = "false";
        } else if ( _stats.compareTo("cOverall") == 0 ){
            _statsFull = "Overall Competition";
            this.cStatsRender = "false";
            this.dStatsRender = "false";
            this.tStatsRender = "false";  
            this.cOverallRender = "true";
        }
        
        FacesMessage msg = new FacesMessage(FacesMessage.SEVERITY_INFO, "Statistics:", _statsFull);  
        FacesContext.getCurrentInstance().addMessage(null, msg);  
    }
}
