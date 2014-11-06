/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package entity;

import java.io.Serializable;
import java.util.List;
import javax.persistence.*;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;

/**
 *
 * @author mbaty001
 */
@Entity
@Table(name = "SU")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Su.findAll", query = "SELECT s FROM Su s"),
    @NamedQuery(name = "Su.findByIdSU", query = "SELECT s FROM Su s WHERE s.idSU = :idSU"),
    @NamedQuery(name = "Su.findBySuFrom", query = "SELECT s FROM Su s WHERE s.suFrom = :suFrom"),
    @NamedQuery(name = "Su.findBySuTo", query = "SELECT s FROM Su s WHERE s.suTo = :suTo"),
    @NamedQuery(name = "Su.findBySuStartTime", query = "SELECT s FROM Su s WHERE s.suStartTime = :suStartTime"),
    @NamedQuery(name = "Su.findBySuEndTime", query = "SELECT s FROM Su s WHERE s.suEndTime = :suEndTime")})
public class Su implements Serializable {
    @Basic(optional = false)
    @NotNull
    @Column(name = "SU_ERRORS")
    private int suErrors;
    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Column(name = "idSU")
    private Integer idSU;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 2000000000)
    @Column(name = "SU_FROM")
    private String suFrom;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 2000000000)
    @Column(name = "SU_TO")
    private String suTo;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 2000000000)
    @Column(name = "SU_START_TIME")
    private String suStartTime;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 2000000000)
    @Column(name = "SU_END_TIME")
    private String suEndTime;
    @JoinColumn(name = "LAB_idLAB", referencedColumnName = "idLAB")
    @ManyToOne(optional = false)
    private Lab lABidLAB;
    @JoinColumn(name = "SU_STATE_idSU_STATE", referencedColumnName = "idSU_STATE")
    @ManyToOne(optional = false)
    private SuState sUSTATEidSUSTATE;
    @JoinColumn(name = "SU_TYPE_idSU_TYPE", referencedColumnName = "idSU_TYPE")
    @ManyToOne(optional = false)
    private SuType sUTYPEidSUTYPE;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "sUidSU")
    private List<SuLog> suLogList;

    public Su() {
    }

    public Su(Integer idSU) {
        this.idSU = idSU;
    }

    public Su(Integer idSU, String suFrom, String suTo, String suStartTime, String suEndTime) {
        this.idSU = idSU;
        this.suFrom = suFrom;
        this.suTo = suTo;
        this.suStartTime = suStartTime;
        this.suEndTime = suEndTime;
    }

    public Integer getIdSU() {
        return idSU;
    }

    public void setIdSU(Integer idSU) {
        this.idSU = idSU;
    }

    public String getSuFrom() {
        return suFrom;
    }

    public void setSuFrom(String suFrom) {
        this.suFrom = suFrom;
    }

    public String getSuTo() {
        return suTo;
    }

    public void setSuTo(String suTo) {
        this.suTo = suTo;
    }

    public String getSuStartTime() {
        return suStartTime;
    }

    public void setSuStartTime(String suStartTime) {
        this.suStartTime = suStartTime;
    }

    public String getSuEndTime() {
        return suEndTime;
    }

    public void setSuEndTime(String suEndTime) {
        this.suEndTime = suEndTime;
    }

    public Lab getLABidLAB() {
        return lABidLAB;
    }

    public void setLABidLAB(Lab lABidLAB) {
        this.lABidLAB = lABidLAB;
    }

    public SuState getSUSTATEidSUSTATE() {
        return sUSTATEidSUSTATE;
    }

    public void setSUSTATEidSUSTATE(SuState sUSTATEidSUSTATE) {
        this.sUSTATEidSUSTATE = sUSTATEidSUSTATE;
    }

    public SuType getSUTYPEidSUTYPE() {
        return sUTYPEidSUTYPE;
    }

    public void setSUTYPEidSUTYPE(SuType sUTYPEidSUTYPE) {
        this.sUTYPEidSUTYPE = sUTYPEidSUTYPE;
    }

    //@XmlTransient
    public List<SuLog> getSuLogList() {
        return suLogList;
    }
    
    public void setSuLogList(List<SuLog> suLogList) {
        this.suLogList = suLogList;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (idSU != null ? idSU.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof Su)) {
            return false;
        }
        Su other = (Su) object;
        if ((this.idSU == null && other.idSU != null) || (this.idSU != null && !this.idSU.equals(other.idSU))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "entity.Su[ idSU=" + idSU + " ]";
    }

    public int getSuErrors() {
        return suErrors;
    }

    public void setSuErrors(int suErrors) {
        this.suErrors = suErrors;
    }
    
}
