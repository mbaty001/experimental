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
@Table(name = "MS")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Ms.findAll", query = "SELECT m FROM Ms m"),
    @NamedQuery(name = "Ms.findByIdMS", query = "SELECT m FROM Ms m WHERE m.idMS = :idMS"),
    @NamedQuery(name = "Ms.findByName", query = "SELECT m FROM Ms m WHERE m.name = :name")})
public class Ms implements Serializable {
    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Column(name = "idMS")
    private Integer idMS;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 2000000000)
    @Column(name = "NAME")
    private String name;
    @JoinColumn(name = "LAB_idLAB", referencedColumnName = "idLAB")
    @ManyToOne(optional = false)
    private Lab lABidLAB;
    @JoinColumn(name = "MS_TYPE_idHW_TYPE", referencedColumnName = "idHW_TYPE")
    @ManyToOne(optional = false)
    private HwType mSTYPEidHWTYPE;

    public Ms() {
    }

    public Ms(Integer idMS) {
        this.idMS = idMS;
    }

    public Ms(Integer idMS, String name) {
        this.idMS = idMS;
        this.name = name;
    }

    public Integer getIdMS() {
        return idMS;
    }

    public void setIdMS(Integer idMS) {
        this.idMS = idMS;
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

    public HwType getMSTYPEidHWTYPE() {
        return mSTYPEidHWTYPE;
    }

    public void setMSTYPEidHWTYPE(HwType mSTYPEidHWTYPE) {
        this.mSTYPEidHWTYPE = mSTYPEidHWTYPE;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (idMS != null ? idMS.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof Ms)) {
            return false;
        }
        Ms other = (Ms) object;
        if ((this.idMS == null && other.idMS != null) || (this.idMS != null && !this.idMS.equals(other.idMS))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "entity.Ms[ idMS=" + idMS + " ]";
    }
    
}
