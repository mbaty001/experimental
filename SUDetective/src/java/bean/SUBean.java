/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package bean;

import entity.*;
import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;
import java.io.Serializable;
import java.util.List;
import javax.ejb.Stateless;
import javax.faces.application.FacesMessage;
import javax.faces.context.FacesContext;
import javax.faces.model.SelectItem;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import org.primefaces.event.ToggleEvent;

/**
 *
 * @author mbaty001
 */
@Stateless
public class SUBean implements Serializable {
    
    public static final String PROP_SAMPLE_PROPERTY = "sampleProperty";
    private String sampleProperty;
    private PropertyChangeSupport propertySupport;
    private List<Su> filteredSus;
    
    public SUBean() {
        propertySupport = new PropertyChangeSupport(this);
    }
    
    public String getSampleProperty() {
        return sampleProperty;
    }
    
    public void setSampleProperty(String value) {
        String oldValue = sampleProperty;
        sampleProperty = value;
        propertySupport.firePropertyChange(PROP_SAMPLE_PROPERTY, oldValue, sampleProperty);
    }
    
    public void addPropertyChangeListener(PropertyChangeListener listener) {
        propertySupport.addPropertyChangeListener(listener);
    }
    
    public void removePropertyChangeListener(PropertyChangeListener listener) {
        propertySupport.removePropertyChangeListener(listener);
    }
    
    @PersistenceContext
    EntityManager em;
    
    public List<Su> findAllSu(){
        return em.createNamedQuery("Su.findAll").getResultList();            
    }
    
    public List<SuType> findAllSuType(){
        return em.createNamedQuery("SuType.findAll").getResultList();        
    }
    
    public List<SuState> findAllSuState(){
        return em.createNamedQuery("SuState.findAll").getResultList();
    }
    
    public List<Lab> findAllLab(){
        return em.createNamedQuery("Lab.findAll").getResultList();
    }
        
    public List<SuLog> findLogsBySuId(Integer idSu){
            return em.createQuery("select l from SuLog l where l.SU_idSU = :idSu")
                    .setParameter("idSu", idSu)
                    .getResultList();
    }
    
    public SelectItem[] findSuFromOptions(){
        List<Su> sus = findAllSu();
        SelectItem[] temp = new SelectItem[sus.size() + 1];
        SelectItem tempCmp = null;
        SelectItem _temp = null;
        Boolean goOut = false;
        
        temp[0] = new SelectItem("", "Select"); 
        int i = 1;
        for(Su s: sus){
            goOut = false;
            _temp = new SelectItem(s.getSuFrom(), s.getSuFrom());
            for (int j=1; j<i; j++){                
                if ( _temp.getValue().equals(temp[j].getValue()) ){
                    goOut = true;
                    break;
                }
            }
            if (goOut == false){
                temp[i] = _temp;
                i += 1;
            }
        }
        
        SelectItem[] returnArray = new SelectItem[i];
        System.arraycopy(temp, 0, returnArray, 0, i);
                        
        for (int j=1; j<i-1; j++)
            for(int k=j; k<i; k++){
                if (returnArray[j].getLabel().compareTo(returnArray[k].getLabel()) > 0 ){
                    tempCmp = returnArray[j];
                    returnArray[j] = returnArray[k];
                    returnArray[k] = tempCmp;
                }
                    
            }
        return returnArray;
    }
    
    public SelectItem[] findSuToOptions(){
        List<Su> sus = findAllSu();
        SelectItem[] temp = new SelectItem[sus.size() + 1];
        SelectItem tempCmp = null;
        SelectItem _temp = null;
        Boolean goOut = false;
        
        temp[0] = new SelectItem("", "Select"); 
        int i = 1;
        for(Su s: sus){
            goOut = false;
            _temp = new SelectItem(s.getSuTo(), s.getSuTo());
            for (int j=1; j<i; j++){                
                if ( _temp.getValue().equals(temp[j].getValue()) ){
                    goOut = true;
                    break;
                }
            }
            if (goOut == false){
                temp[i] = _temp;
                i += 1;
            }
        }
        SelectItem[] returnArray = new SelectItem[i];
        System.arraycopy(temp, 0, returnArray, 0, i);
                        
        for (int j=1; j<i-1; j++)
            for(int k=j; k<i; k++){
                if (returnArray[j].getLabel().compareTo(returnArray[k].getLabel()) > 0 ){
                    tempCmp = returnArray[j];
                    returnArray[j] = returnArray[k];
                    returnArray[k] = tempCmp;
                }                    
            }
        return returnArray;
    }
    
    public SelectItem[] findSuTypeOptions(){
        List<SuType> st = findAllSuType();
        SelectItem[] temp = new SelectItem[st.size() + 1];
        SelectItem tempCmp = null;
        
        temp[0] = new SelectItem("", "Select"); 
        int i = 1;
        for(SuType s: st){
            temp[i] = new SelectItem(s.getName(), s.getName());
            i += 1;
        }
        
        for (int j=1; j<i-1; j++)
            for(int k=j; k<i; k++){
                if (temp[j].getLabel().compareTo(temp[k].getLabel()) > 0 ){
                    tempCmp = temp[j];
                    temp[j] = temp[k];
                    temp[k] = tempCmp;
                }                    
            }
        return temp;
    }
    
    public SelectItem[] findSuStateOptions(){
        List<SuState> ss = findAllSuState();
        SelectItem[] temp = new SelectItem[ss.size() + 1];
        SelectItem tempCmp = null;

        temp[0] = new SelectItem("", "Select"); 
        int i = 1;
        for(SuState s: ss){
            temp[i] = new SelectItem(s.getName(), s.getName());
            i += 1;
        }
        
        for (int j=1; j<i-1; j++)
            for(int k=j; k<i; k++){
                if (temp[j].getLabel().compareTo(temp[k].getLabel()) > 0 ){
                    tempCmp = temp[j];
                    temp[j] = temp[k];
                    temp[k] = tempCmp;
                }                    
            }
        return temp;
    }
    
    public SelectItem[] findLabOptions(){
        List<Lab> ll = findAllLab();
        SelectItem[] temp = new SelectItem[ll.size() + 1];
        SelectItem tempCmp = null;
        SelectItem _temp = null;
        Boolean goOut = false;

        temp[0] = new SelectItem("", "Select"); 
        int i = 1;
        for(Lab l: ll){
            goOut = false;
            _temp = new SelectItem(l.getName(), l.getName());
            for (int j=1; j<i; j++){                
                if ( _temp.getValue().equals(temp[j].getValue()) ){
                    goOut = true;
                    break;
                }
            }
            if (goOut == false){
                temp[i] = _temp;
                i += 1;
            }            
        }
        
        SelectItem[] returnArray = new SelectItem[i];
        System.arraycopy(temp, 0, returnArray, 0, i);
                        
        for (int j=1; j<i-1; j++)
            for(int k=j; k<i; k++){
                if (returnArray[j].getLabel().compareTo(returnArray[k].getLabel()) > 0 ){
                    tempCmp = returnArray[j];
                    returnArray[j] = returnArray[k];
                    returnArray[k] = tempCmp;
                }                    
            }
        return returnArray;
    }       
}
