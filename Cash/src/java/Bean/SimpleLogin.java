/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Bean;

import java.io.Serializable;
import javax.faces.application.FacesMessage;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.SessionScoped;
import javax.faces.context.FacesContext;

/**
 *
 * @author mbaty001
 */
@ManagedBean
@SessionScoped
public class SimpleLogin implements Serializable{
    String loginname;
    String password;
    String next;
    String logIn;
    String invalidPasswd;
    
    public SimpleLogin(){
        this.loginname = "";
        this.password = "";
        this.next = "";
        this.logIn = "false";
        this.invalidPasswd = "false";
    }

    public String getLoginname() {
        return loginname;
    }

    public void setLoginname(String loginname) {
        this.loginname = loginname;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getNext() {
        return next;
    }

    public void setNext(String next) {
        this.next = next;
    }

    public String getLogIn() {
        return logIn;
    }

    public void setLogIn(String logIn) {
        this.logIn = logIn;
    }

    public String getInvalidPasswd() {
        return invalidPasswd;
    }

    public void setInvalidPasswd(String invalidPasswd) {
        this.invalidPasswd = invalidPasswd;
    }        
    
    public String CheckValidUser(){
        System.out.println("NEXT: " + this.getNext());
        
        if ( this.getLogIn().equals("true") || this.getNext().equals("index.xhtml") || this.getNext().equals("stats.xhtml") ){
            System.out.println("Already logged in");
            System.out.println("RETURNS: " + this.getNext());
            return this.getNext().toString();
        } else {
            System.out.println("login: " + this.getLoginname());
            System.out.println("passwd: " + this.getPassword());
            if (loginname.equals("") && password.equals("")) {
                this.setLogIn("fail");
                System.out.println("RETURNS admin");
                return "admin.xhtml";
            } else {
                if (loginname.equals("admin") && password.equals("kuku")) {
                    this.setLogIn("true");
                    System.out.println("RETURNS: " + this.getNext());
                    return this.getNext().toString();
                } else {
                    FacesMessage msg = new FacesMessage(FacesMessage.SEVERITY_ERROR, "Login incorrect", "Login: " + this.getLoginname() + " pass: " + this.getPassword());
                    FacesContext.getCurrentInstance().addMessage(null, msg); 
                    this.setLoginname("");
                    this.setPassword("");
                    this.setLogIn("fail");
                    this.setInvalidPasswd("true");
                    System.out.println("RETURNS FAIL");                    
                    return "admin.xhtml";
                }
            } 
       }
        
    }    
}
