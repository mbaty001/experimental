/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package entity;

import java.io.Serializable;
import javax.persistence.*;
import javax.xml.bind.annotation.XmlRootElement;

/**
 *
 * @author mbaty001
 */
@Entity
@Table(name = "cash")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Cash.findAll", query = "SELECT c FROM Cash c"),
    @NamedQuery(name = "Cash.findByYear", query = "SELECT c FROM Cash c WHERE c.cashPK.year = :year"),
    @NamedQuery(name = "Cash.findByMonth", query = "SELECT c FROM Cash c WHERE c.cashPK.month = :month"),
    @NamedQuery(name = "Cash.findByU1year", query = "SELECT c FROM Cash c WHERE c.u1year = :u1year"),
    @NamedQuery(name = "Cash.findByU1month", query = "SELECT c FROM Cash c WHERE c.u1month = :u1month"),
    @NamedQuery(name = "Cash.findByU1day", query = "SELECT c FROM Cash c WHERE c.u1day = :u1day"),
    @NamedQuery(name = "Cash.findByU1hour", query = "SELECT c FROM Cash c WHERE c.u1hour = :u1hour"),
    @NamedQuery(name = "Cash.findByU1minute", query = "SELECT c FROM Cash c WHERE c.u1minute = :u1minute"),
    @NamedQuery(name = "Cash.findByU2year", query = "SELECT c FROM Cash c WHERE c.u2year = :u2year"),
    @NamedQuery(name = "Cash.findByU2month", query = "SELECT c FROM Cash c WHERE c.u2month = :u2month"),
    @NamedQuery(name = "Cash.findByU2day", query = "SELECT c FROM Cash c WHERE c.u2day = :u2day"),
    @NamedQuery(name = "Cash.findByU2hour", query = "SELECT c FROM Cash c WHERE c.u2hour = :u2hour"),
    @NamedQuery(name = "Cash.findFullYears", query = "SELECT c.cashPK.year FROM Cash c GROUP BY c.cashPK.year HAVING COUNT(c) > 11"),
    @NamedQuery(name = "Cash.findByMY", query = "SELECT c FROM Cash c WHERE (c.cashPK.month = :month) AND (c.cashPK.year = :year)"),   
    @NamedQuery(name = "Cash.findByM", query = "SELECT c FROM Cash c WHERE c.cashPK.month = :month"),
    @NamedQuery(name = "Cash.findByU2minute", query = "SELECT c FROM Cash c WHERE c.u2minute = :u2minute")})    
public class Cash implements Serializable {
    private static final long serialVersionUID = 1L;
    @EmbeddedId
    protected CashPK cashPK;
    @Column(name = "u1year")
    private Integer u1year;
    @Column(name = "u1month")
    private Integer u1month;
    @Column(name = "u1day")
    private Integer u1day;
    @Column(name = "u1hour")
    private Integer u1hour;
    @Column(name = "u1minute")
    private Integer u1minute;
    @Column(name = "u2year")
    private Integer u2year;
    @Column(name = "u2month")
    private Integer u2month;
    @Column(name = "u2day")
    private Integer u2day;
    @Column(name = "u2hour")
    private Integer u2hour;
    @Column(name = "u2minute")
    private Integer u2minute;
    @JoinColumn(name = "u2id", referencedColumnName = "id")
    @ManyToOne
    private User user1;
    @JoinColumn(name = "u1id", referencedColumnName = "id")
    @ManyToOne
    private User user2;

    public Cash() {
    }

    public Cash(CashPK cashPK) {
        this.cashPK = cashPK;
    }

    public Cash(int year, int month) {
        this.cashPK = new CashPK(year, month);
    }

    public CashPK getCashPK() {
        return cashPK;
    }

    public void setCashPK(CashPK cashPK) {
        this.cashPK = cashPK;
    }

    public Integer getU1year() {
        return u1year;
    }

    public void setU1year(Integer u1year) {
        this.u1year = u1year;
    }

    public Integer getU1month() {
        return u1month;
    }

    public void setU1month(Integer u1month) {
        this.u1month = u1month;
    }

    public Integer getU1day() {
        return u1day;
    }

    public void setU1day(Integer u1day) {
        this.u1day = u1day;
    }

    public Integer getU1hour() {
        return u1hour;
    }

    public void setU1hour(Integer u1hour) {
        this.u1hour = u1hour;
    }

    public Integer getU1minute() {
        return u1minute;
    }

    public void setU1minute(Integer u1minute) {
        this.u1minute = u1minute;
    }

    public Integer getU2year() {
        return u2year;
    }

    public void setU2year(Integer u2year) {
        this.u2year = u2year;
    }

    public Integer getU2month() {
        return u2month;
    }

    public void setU2month(Integer u2month) {
        this.u2month = u2month;
    }

    public Integer getU2day() {
        return u2day;
    }

    public void setU2day(Integer u2day) {
        this.u2day = u2day;
    }

    public Integer getU2hour() {
        return u2hour;
    }

    public void setU2hour(Integer u2hour) {
        this.u2hour = u2hour;
    }

    public Integer getU2minute() {
        return u2minute;
    }

    public void setU2minute(Integer u2minute) {
        this.u2minute = u2minute;
    }

    public User getUser1() {
        return user1;
    }

    public void setUser1(User user) {
        this.user1 = user;
    }

    public User getUser2() {
        return user2;
    }

    public void setUser2(User user) {
        this.user2 = user;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (cashPK != null ? cashPK.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof Cash)) {
            return false;
        }
        Cash other = (Cash) object;
        if ((this.cashPK == null && other.cashPK != null) || (this.cashPK != null && !this.cashPK.equals(other.cashPK))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "entity.Cash[ cashPK=" + cashPK + " ]";
    }
    
}
