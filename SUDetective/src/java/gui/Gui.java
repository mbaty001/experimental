/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package gui;
import bean.SUBean;
import entity.Lab;
import entity.Su;
import entity.SuLog;
import java.io.IOException;
import java.util.List;
import javax.ejb.EJB;
import javax.faces.application.FacesMessage;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.ManagedProperty;
import javax.faces.bean.RequestScoped;
import javax.faces.bean.SessionScoped;
import javax.faces.context.ExternalContext;
import javax.faces.context.FacesContext;
import javax.faces.model.SelectItem;
import org.primefaces.event.ToggleEvent;


/**
 *
 * @author mbaty001
 */
@ManagedBean
@SessionScoped
public class Gui {
    
    @EJB
    SUBean enc;    
    String timeline;
    String node;
    
    public List<Su> getSus(){
        return enc.findAllSu();
    }
    
    public SelectItem[] getSuFromOptions(){
        return enc.findSuFromOptions();
    }
    
    public SelectItem[] getSuToOptions(){
        return enc.findSuToOptions();
    }
        
    public SelectItem[] getSuTypeOptions(){
        return enc.findSuTypeOptions();
    }
    
    public SelectItem[] getSuStateOptions(){
        return enc.findSuStateOptions();
    }
    
    public SelectItem[] getLabOptions(){
        return enc.findLabOptions();
    }
    
    public List<Lab> getLabs(){
        return enc.findAllLab();
    }
    
    public List<SuLog> getLogsBySuId(Integer idSu){
        return enc.findLogsBySuId(idSu);
    }
        
    public void onRowToggle(ToggleEvent event) {  
        FacesMessage msg = new FacesMessage(FacesMessage.SEVERITY_INFO, "SU and Lab details", "");          
        FacesContext.getCurrentInstance().addMessage(null, msg);  
    }
    
    public void timelineChoose() throws IOException{
        ExternalContext externalContext = FacesContext.getCurrentInstance().getExternalContext();
                
        externalContext.redirect("timeline.xhtml");
    }
    
    public void setTimeline(String timeline){
        this.timeline = timeline;
    }    
    
    public String getTimeline(){
        return this.timeline;
    }
    
    public void setNode(String node){
        this.node = node;
    }
    
    public String getNode(){
        return this.node;
    }    
}
