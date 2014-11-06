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
@Table(name = "SU_TYPE")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "SuType.findAll", query = "SELECT s FROM SuType s"),
    @NamedQuery(name = "SuType.findByIdSUTYPE", query = "SELECT s FROM SuType s WHERE s.idSUTYPE = :idSUTYPE"),
    @NamedQuery(name = "SuType.findByName", query = "SELECT s FROM SuType s WHERE s.name = :name")})
public class SuType implements Serializable, Comparable<SuType> {
    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Column(name = "idSU_TYPE")
    private Integer idSUTYPE;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 2000000000)
    @Column(name = "NAME")
    private String name;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "sUTYPEidSUTYPE")
    private List<Su> suList;

    public int compareTo(SuType st){
        return name.compareTo(st.name);
    }
    
    public SuType() {
    }

    public SuType(Integer idSUTYPE) {
        this.idSUTYPE = idSUTYPE;
    }

    public SuType(Integer idSUTYPE, String name) {
        this.idSUTYPE = idSUTYPE;
        this.name = name;
    }

    public Integer getIdSUTYPE() {
        return idSUTYPE;
    }

    public void setIdSUTYPE(Integer idSUTYPE) {
        this.idSUTYPE = idSUTYPE;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @XmlTransient
    public List<Su> getSuList() {
        return suList;
    }

    public void setSuList(List<Su> suList) {
        this.suList = suList;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (idSUTYPE != null ? idSUTYPE.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof SuType)) {
            return false;
        }
        SuType other = (SuType) object;
        if ((this.idSUTYPE == null && other.idSUTYPE != null) || (this.idSUTYPE != null && !this.idSUTYPE.equals(other.idSUTYPE))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "entity.SuType[ idSUTYPE=" + idSUTYPE + " ]";
    }
    
}
