/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Bean;

import entity.Cash;
import entity.User;
import java.io.Serializable;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.List;
import javax.ejb.Stateful;
import javax.faces.application.FacesMessage;
import javax.faces.context.FacesContext;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;

/**
 *
 * @author mbaty001
 */
@Stateful
public class CashBean implements Serializable{
    
    @PersistenceContext
    EntityManager em;
    
    public CashBean(){
        
    }
    
    public List<Cash> findAll(){        
        return em.createNamedQuery("Cash.findAll").getResultList();
    }
    
    public void saveCash(Cash c){
        em.merge(c);
    }
    
    public List<User> findAllUsers(){
        return em.createNamedQuery("User.findAll").getResultList();
    }
    
    public List<String> findAllUserNames(){
        List<User> _userList;
        ArrayList<String> _nameList = new ArrayList<String>();
        
        _userList =  em.createNamedQuery("User.findAll").getResultList();
        for(User u: _userList){
            _nameList.add(u.getName());
        }
        
        return _nameList;
    }
    
    public List<Integer> findFullYears(){
        return em.createNamedQuery("Cash.findFullYears").getResultList();
    }
    
    public List<Cash> findByMonthYear(int _month, int _year){        
        return  em.createNamedQuery("Cash.findByMY")
                .setParameter("month", _month)
                .setParameter("year", _year)
                .getResultList();        
    }
    
    public User findUserByName(String _name){
        return (User) em.createNamedQuery("User.findByName")
                .setParameter("name", _name)
                .getSingleResult();
    }
                     
    public ArrayList<Kuku> setEverything() throws ParseException{
        
        Kuku wrPtr;
        Kuku erPtr;
        Kuku orPtr;
    
        ArrayList<Kuku> retList = new ArrayList<Kuku>();
        List<Cash> cashList = em.createNamedQuery("Cash.findAll").getResultList();
               
        for (Cash c: cashList){
            try{
                retList.add(new Kuku(c.getUser1().getName(), c.getU1year().toString(), c.getU1month().toString(), 
                           c.getU1day().toString(), c.getU1hour().toString(), c.getU1minute().toString(),
                           c.getUser2().getName(), c.getU2year().toString(), c.getU2month().toString(), 
                           c.getU2day().toString(), c.getU2hour().toString(), c.getU2minute().toString()));
            } catch (ParseException e){
                System.out.println(e.toString());
            }
        }
        
        /*
         * Set World, Europien, Olimpic records
         */
        
        wrPtr = retList.get(0);
        erPtr = retList.get(0);
        orPtr = retList.get(0);
        for (Kuku k: retList){           
            if (k.compareTo(wrPtr) > 0){
                orPtr = erPtr;
                erPtr = wrPtr;
                wrPtr = k;
            }
            else if (k.compareTo(erPtr) > 0){
                    orPtr = erPtr;
                    erPtr = k;
                 }
                 else if (k.compareTo(orPtr) > 0){
                    orPtr = k;
                }            
        }
  
        if (wrPtr != null){
            wrPtr.setRecord(Boolean.TRUE);
            if (wrPtr.getOneOrTwo() == 1)
                wrPtr.setU1value(wrPtr.getU1value() + " WR");
            else
                wrPtr.setU2value(wrPtr.getU2value() + " WR");
        }
        
        if (erPtr != null){
            erPtr.setRecord(Boolean.TRUE);
            if (erPtr.getOneOrTwo() == 1)
                erPtr.setU1value(erPtr.getU1value() + " ER");
            else
                erPtr.setU2value(erPtr.getU2value() + " ER");
        }
        
        if (orPtr != null){
            orPtr.setRecord(Boolean.TRUE);
            if (orPtr.getOneOrTwo() == 1)
                orPtr.setU1value(orPtr.getU1value() + " OR");
            else
                orPtr.setU2value(orPtr.getU2value() + " OR");
        }   
        return retList;
    }        
   
    public void persistCash(Cash _c){
        em.merge(_c);
    }
    
    public ArrayList<Integer> getNoOfWins(List<Kuku> _kukuList){
    
        int _michalWins = 0;
        int _przemekWins = 0;
        
        ArrayList<Integer> _noOfWins = new ArrayList<Integer>();
    
        for (Kuku k: _kukuList){ 
            if (k.getOneOrTwo() == 1) 
                _michalWins++;
            else
                _przemekWins++;            
        }
        _noOfWins.add(_przemekWins);
        _noOfWins.add(_michalWins);
            
        return _noOfWins;
    }

}
