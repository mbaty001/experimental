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
@Table(name = "HW_TYPE")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "HwType.findAll", query = "SELECT h FROM HwType h"),
    @NamedQuery(name = "HwType.findByIdHWTYPE", query = "SELECT h FROM HwType h WHERE h.idHWTYPE = :idHWTYPE"),
    @NamedQuery(name = "HwType.findByName", query = "SELECT h FROM HwType h WHERE h.name = :name")})
public class HwType implements Serializable {
    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Column(name = "idHW_TYPE")
    private Integer idHWTYPE;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 2000000000)
    @Column(name = "NAME")
    private String name;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "aCSTYPEidHWTYPE")
    private List<Lab> labList;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "hWTYPEidHWTYPE")
    private List<SuLog> suLogList;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "tSTYPEidHWTYPE")
    private List<Ts> tsList;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "mSTYPEidHWTYPE")
    private List<Ms> msList;

    public HwType() {
    }

    public HwType(Integer idHWTYPE) {
        this.idHWTYPE = idHWTYPE;
    }

    public HwType(Integer idHWTYPE, String name) {
        this.idHWTYPE = idHWTYPE;
        this.name = name;
    }

    public Integer getIdHWTYPE() {
        return idHWTYPE;
    }

    public void setIdHWTYPE(Integer idHWTYPE) {
        this.idHWTYPE = idHWTYPE;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @XmlTransient
    public List<Lab> getLabList() {
        return labList;
    }

    public void setLabList(List<Lab> labList) {
        this.labList = labList;
    }

    @XmlTransient
    public List<SuLog> getSuLogList() {
        return suLogList;
    }

    public void setSuLogList(List<SuLog> suLogList) {
        this.suLogList = suLogList;
    }

    @XmlTransient
    public List<Ts> getTsList() {
        return tsList;
    }

    public void setTsList(List<Ts> tsList) {
        this.tsList = tsList;
    }

    @XmlTransient
    public List<Ms> getMsList() {
        return msList;
    }

    public void setMsList(List<Ms> msList) {
        this.msList = msList;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (idHWTYPE != null ? idHWTYPE.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof HwType)) {
            return false;
        }
        HwType other = (HwType) object;
        if ((this.idHWTYPE == null && other.idHWTYPE != null) || (this.idHWTYPE != null && !this.idHWTYPE.equals(other.idHWTYPE))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "entity.HwType[ idHWTYPE=" + idHWTYPE + " ]";
    }
    
}
