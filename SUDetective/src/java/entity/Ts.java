/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package entity;

import java.io.Serializable;
import javax.persistence.*;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;

/**
 *
 * @author mbaty001
 */
@Entity
@Table(name = "TS")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Ts.findAll", query = "SELECT t FROM Ts t"),
    @NamedQuery(name = "Ts.findByIdTS", query = "SELECT t FROM Ts t WHERE t.idTS = :idTS"),
    @NamedQuery(name = "Ts.findByName", query = "SELECT t FROM Ts t WHERE t.name = :name")})
public class Ts implements Serializable {
    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Column(name = "idTS")
    private Integer idTS;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 2000000000)
    @Column(name = "NAME")
    private String name;
    @JoinColumn(name = "LAB_idLAB", referencedColumnName = "idLAB")
    @ManyToOne(optional = false)
    private Lab lABidLAB;
    @JoinColumn(name = "TS_TYPE_idHW_TYPE", referencedColumnName = "idHW_TYPE")
    @ManyToOne(optional = false)
    private HwType tSTYPEidHWTYPE;

    public Ts() {
    }

    public Ts(Integer idTS) {
        this.idTS = idTS;
    }

    public Ts(Integer idTS, String name) {
        this.idTS = idTS;
        this.name = name;
    }

    public Integer getIdTS() {
        return idTS;
    }

    public void setIdTS(Integer idTS) {
        this.idTS = idTS;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Lab getLABidLAB() {
        return lABidLAB;
    }

    public void setLABidLAB(Lab lABidLAB) {
        this.lABidLAB = lABidLAB;
    }

    public HwType getTSTYPEidHWTYPE() {
        return tSTYPEidHWTYPE;
    }

    public void setTSTYPEidHWTYPE(HwType tSTYPEidHWTYPE) {
        this.tSTYPEidHWTYPE = tSTYPEidHWTYPE;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (idTS != null ? idTS.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof Ts)) {
            return false;
        }
        Ts other = (Ts) object;
        if ((this.idTS == null && other.idTS != null) || (this.idTS != null && !this.idTS.equals(other.idTS))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "entity.Ts[ idTS=" + idTS + " ]";
    }
    
}
